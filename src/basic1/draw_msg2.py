#!/usr/bin/env python3
import sys
import re

def get_doc_data(url: str) -> str:
    pass

def parse_points(text: str):
    points = {}
    for idx, line in enumerate(text.splitlines(), 1):
        [x, ch, y] = line.split(sep= '|')
        points[(x, y)] = ch
    if not points:
        raise ValueError("No valid coordinate lines.")
    return points

def build_grid(points: dict, invert_y: bool = False):
    xs = [x for (x,y) in points.keys()]
    ys = [y for (x,y) in points.keys()]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    width = max_x - min_x + 1
    height = max_y - min_y + 1

    grid = [[" " for _ in range(width)] for _ in range(height)]
    for (x, y), ch in points.items():
        col = x - min_x
        row = y - min_y
        if 0 <= row < height and 0 <= col < width:
            grid[row][col] = ch
    return grid

def render_grid(grid):
    return "\n".join("".join(row) for row in grid)

def main():

    URL = "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"
    text = get_doc_data(URL)
    text = "................."
    points = parse_points(text)
    grid = build_grid(points)
    print(render_grid(grid))

if __name__ == "__main__":
    main()
