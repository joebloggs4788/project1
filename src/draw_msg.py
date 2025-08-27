#!/usr/bin/env python3
import sys
import re
import shlex
from html.parser import HTMLParser
from urllib.request import urlopen, Request
import html


DOC_URL = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"


class _HTMLToText(HTMLParser):
    """Minimal HTML-to-text extractor that preserves line breaks."""
    def __init__(self):
        super().__init__()
        self._out = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "br":
            self._out.append("\n")

    def handle_endtag(self, tag):
        if tag.lower() in ("p", "div", "li", "h1", "h2", "h3", "h4", "h5"):
            self._out.append("\n")

    def handle_data(self, data):
        self._out.append(data)

    def text(self):
        return html.unescape("".join(self._out))


def fetch_text(url: str) -> str:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req) as resp:
        raw = resp.read().decode("utf-8", errors="replace")
    parser = _HTMLToText()
    parser.feed(raw)
    return parser.text()


def decode_char_token(token: str) -> str:
    """Turn a token into a Unicode character/string."""
    s = token.strip()

    # Named "space"
    if s.lower() in {"space", "blank"}:
        return " "

    # U+XXXX form
    m = re.fullmatch(r"U\+([0-9A-Fa-f]+)", s)
    if m:
        return chr(int(m.group(1), 16))

    # Hex codepoint like 0x2588
    if re.fullmatch(r"0x[0-9A-Fa-f]+", s):
        return chr(int(s, 16))

    # Quoted content (strip only outer quotes if present)
    if (len(s) >= 2) and ((s[0] == s[-1]) and s[0] in ("'", '"')):
        s = s[1:-1]

    # Decode common escape sequences like \u2588, \n, \t, \N{...}
    try:
        s = bytes(s, "utf-8").decode("unicode_escape")
    except Exception:
        pass

    return s if s else " "


def extract_xy_from_labels(line: str):
    """Try labeled forms like x=12 y=7 char='█'."""
    x = y = None
    m = re.search(r"\bx\s*[:=]\s*(-?\d+)\b", line, re.I)
    if m:
        x = int(m.group(1))
    m = re.search(r"\by\s*[:=]\s*(-?\d+)\b", line, re.I)
    if m:
        y = int(m.group(1))
    # Character if explicitly labeled
    m = re.search(r"\bchar(?:acter)?\s*[:=]\s*(.+?)\s*$", line, re.I)
    ch = None
    if m:
        ch = decode_char_token(m.group(1).strip())
    return x, y, ch


def parse_line_to_point(line: str):
    """Return (x, y, ch) or None if unparseable."""
    original = line
    line = line.strip()
    if not line or line.startswith("#"):
        return None

    # Try labeled extraction first
    x, y, ch = extract_xy_from_labels(line)
    if x is not None and y is not None:
        if ch is None:
            # If no explicit char label, try to find quoted or U+ token
            m = re.search(r"(['\"]).*?\1", line)
            if m:
                ch = decode_char_token(m.group(0))
            else:
                m = re.search(r"U\+[0-9A-Fa-f]+", line)
                if m:
                    ch = decode_char_token(m.group(0))
        if ch is None:
            # Fall back to last non-numeric token
            toks = [t for t in shlex.split(line) if not re.fullmatch(r"[-+]?\d+", t)]
            ch = decode_char_token(toks[-1]) if toks else " "
        return (x, y, ch)

    # Unlabeled: use shlex to respect quotes
    try:
        toks = shlex.split(line)
    except ValueError:
        toks = line.split()

    # Heuristic: first two integers are x and y; the rest is the character token
    ints = []
    others = []
    for t in toks:
        if re.fullmatch(r"[-+]?\d+", t):
            ints.append(int(t))
        else:
            others.append(t)

    if len(ints) >= 2:
        x, y = ints[0], ints[1]
        # Prefer a quoted/U+ token if present
        quoted = re.findall(r"(['\"]).*?\1", original)
        if quoted:
            ch = decode_char_token(quoted[0])
        else:
            # If there are non-integer tokens, join them (allow multi-codepoint glyphs)
            ch_token = others[0] if others else (toks[2] if len(toks) >= 3 else " ")
            ch = decode_char_token(ch_token)
        return (x, y, ch)

    # As a last resort, scan for two integers in the raw line
    nums = re.findall(r"[-+]?\d+", line)
    if len(nums) >= 2:
        x, y = int(nums[0]), int(nums[1])
        m = re.search(r"U\+[0-9A-Fa-f]+", line)
        if m:
            ch = decode_char_token(m.group(0))
        else:
            m = re.search(r"(['\"]).*?\1", line)
            ch = decode_char_token(m.group(0)) if m else " "
        return (x, y, ch)

    return None


def parse_points(text: str):
    points = {}
    for idx, line in enumerate(text.splitlines(), 1):
        pt = parse_line_to_point(line)
        if pt is None:
            continue
        x, y, ch = pt
        points[(x, y)] = ch  # last one wins if duplicate
    if not points:
        raise ValueError("No coordinates parsed. Check the document format.")
    return points


def build_grid(points: dict, invert_y: bool = False):
    xs = [x for (x, _y) in points.keys()]
    ys = [y for (_x, y) in points.keys()]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    width = max_x - min_x + 1
    height = max_y - min_y + 1

    # Prepare grid filled with spaces
    grid = [[" " for _ in range(width)] for _ in range(height)]

    for (x, y), ch in points.items():
        col = x - min_x
        row = (max_y - y) if invert_y else (y - min_y)
        if 0 <= row < height and 0 <= col < width:
            # Place the full string; if longer than 1, it will occupy multiple columns visually
            grid[row][col] = ch

    return grid


def render_grid(grid):
    return "\n".join("".join(row) for row in grid)


def main():
    # Usage: script.py [URL] [--invert-y]
    url = DOC_URL
    invert_y = False
    for arg in sys.argv[1:]:
        if arg == "--invert-y":
            invert_y = True
        elif arg.startswith("-"):
            print(f"Unknown option: {arg}", file=sys.stderr)
        else:
            url = arg

    text = fetch_text(url)
    points = parse_points(text)
    grid = build_grid(points, invert_y=invert_y)
    print(render_grid(grid))


if __name__ == "__main__":
    main()

