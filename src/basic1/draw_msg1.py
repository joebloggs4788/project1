#!/usr/bin/env python3
import sys
import re
import html
from urllib.parse import urlparse, urlunparse, urlencode, parse_qsl
from urllib.request import urlopen, Request

MAX_CELLS = 2_000_000  # safety guard against accidental giant grids
USER_AGENT = "Mozilla/5.0"

def is_url(s: str) -> bool:
    return "://" in s

def add_query_param(url: str, **params) -> str:
    parts = list(urlparse(url))
    q = dict(parse_qsl(parts[4]))
    q.update(params)
    parts[4] = urlencode(q)
    return urlunparse(parts)

def candidates_for_plain_text(url: str):
    """Yield best-guess plain-text endpoints for a Google Doc URL."""
    u = url.strip()
    # 1) If it's the normal doc link with /document/d/<ID>/...
    m = re.search(r"/document/d/([^/]+)/", u)
    if m:
        doc_id = m.group(1)
        yield f"https://docs.google.com/document/d/{doc_id}/export?format=txt"

    # 2) If it's a published link /document/d/e/<PUBID>/pub
    if re.search(r"/document/d/e/[^/]+/pub", u):
        # Try explicit output=txt first
        yield add_query_param(u, output="txt")
        # Some deployments accept format=txt
        yield add_query_param(u, format="txt")

    # 3) As a last resort, try the URL as-is (may already be a text export)
    yield u

def fetch_text(url: str) -> str:
    """Try to fetch plain text; reject HTML unless absolutely necessary."""
    last_error = None
    for cand in candidates_for_plain_text(url):
        try:
            req = Request(cand, headers={"User-Agent": USER_AGENT})
            with urlopen(req, timeout=20) as resp:
                raw = resp.read()
                encoding = resp.headers.get_content_charset() or "utf-8"
                text = raw.decode(encoding, errors="replace")
                ctype = resp.headers.get("Content-Type", "").lower()
            # Prefer true text/plain
            if "text/plain" in ctype:
                return text
            # If not labeled text/plain, reject obvious HTML
            if "<html" in text.lower() and "</html>" in text.lower():
                last_error = f"Got HTML from {cand}"
                continue
            # If it looks like plain lines, accept
            return html.unescape(text)
        except Exception as e:
            last_error = f"{type(e).__name__}: {e}"
            continue
    raise RuntimeError(f"Could not fetch plain text. Last error: {last_error}")

# --- Parsing ---

INT = r"[-+]?\d+"

def decode_char_token(token: str) -> str:
    s = token.strip()
    # Quoted single token
    if len(s) >= 2 and s[0] == s[-1] and s[0] in ("'", '"'):
        s = s[1:-1]
    # U+XXXX
    m = re.fullmatch(r"U\+([0-9A-Fa-f]+)", s)
    if m:
        return chr(int(m.group(1), 16))
    # 0xXXXX
    if re.fullmatch(r"0x[0-9A-Fa-f]+", s):
        return chr(int(s, 16))
    # Escapes like \u2588
    try:
        s = bytes(s, "utf-8").decode("unicode_escape")
    except Exception:
        pass
    return s if s else " "

def parse_line(line: str):
    """Strictly accept only clear patterns to avoid garbage:
       - x=INT y=INT char=...
       - y=INT x=INT "..." (any order x/y; char= optional)
       - INT INT CHAR...
    """
    s = line.strip()
    if not s or s.startswith("#"):
        return None

    # labeled x= y= (any order)
    if re.search(r"\bx\s*[:=]\s*" + INT, s, re.I) and re.search(r"\by\s*[:=]\s*" + INT, s, re.I):
        xm = re.search(r"\bx\s*[:=]\s*(" + INT + r")\b", s, re.I)
        ym = re.search(r"\by\s*[:=]\s*(" + INT + r")\b", s, re.I)
        x, y = int(xm.group(1)), int(ym.group(1))
        cm = re.search(r"\bchar(?:acter)?\s*[:=]\s*(.+)$", s, re.I)
        if cm:
            ch = decode_char_token(cm.group(1).strip())
        else:
            # take the last quoted or U+ token; otherwise last non-numeric token
            qm = re.findall(r"(['\"]).*?\1", s)
            if qm:
                ch = decode_char_token(qm[-1])
            else:
                # tokens that are not ints and not labels
                toks = [t for t in re.findall(r"""(?:["'][^"']*["']|\S+)""", s)
                        if not re.fullmatch(INT, t) and not re.match(r"(?i)^(x|y|char|character)\s*[:=]$", t)]
                ch = decode_char_token(toks[-1]) if toks else " "
        return x, y, ch

    # unlabeled: INT INT CHAR...
    m = re.match(r"^\s*(" + INT + r")\s+(" + INT + r")\s+(.+?)\s*$", s)
    if m:
        x, y = int(m.group(1)), int(m.group(2))
        ch = decode_char_token(m.group(3))
        return x, y, ch

    return None

def parse_points(text: str, max_abs=100000):
    points = {}
    for idx, line in enumerate(text.splitlines(), 1):
        pt = parse_line(line)
        if pt is None:
            continue
        x, y, ch = pt
        # basic sanity clamp to avoid wild values from accidental matches
        if abs(x) > max_abs or abs(y) > max_abs:
            continue
        points[(x, y)] = ch
    if not points:
        raise ValueError("No valid coordinate lines found. Ensure lines look like: 'x=1 y=2 char=█' or '1 2 █'")
    return points

# --- Grid build & render ---

def build_grid(points: dict, invert_y: bool = False):
    xs = [x for (x, _y) in points.keys()]
    ys = [y for (_x, y) in points.keys()]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    if width * height > MAX_CELLS:
        raise ValueError(f"Grid too large ({width}x{height} > {MAX_CELLS} cells). Check the source data.")

    grid = [[" " for _ in range(width)] for _ in range(height)]
    for (x, y), ch in points.items():
        col = x - min_x
        row = (max_y - y) if invert_y else (y - min_y)
        if 0 <= row < height and 0 <= col < width:
            grid[row][col] = ch
    return grid

def render_grid(grid):
    return "\n".join("".join(row) for row in grid)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 draw_gdoc_grid.py <gdoc_url_or_txt_file> [--invert-y]")
        sys.exit(2)

    invert_y = False
    target = None
    for a in sys.argv[1:]:
        if a == "--invert-y":
            invert_y = True
        elif target is None:
            target = a

    if target is None:
        print("Provide a Google Doc URL or a local .txt file.")
        sys.exit(2)

    # Accept local .txt file as well
    if not is_url(target):
        with open(target, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = fetch_text(target)

    points = parse_points(text)
    grid = build_grid(points, invert_y=invert_y)
    print(render_grid(grid))

if __name__ == "__main__":
    main()
