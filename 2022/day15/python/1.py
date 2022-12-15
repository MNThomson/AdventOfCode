#!/usr/bin/env python3

import re

score_1 = 0
scan_view = {}
sigs_beacs = {}
fullview = {}

at_row = set()
target_row = 2_000_000


def print_board():
    max_r = min_r = 0
    max_c = min_c = 0
    for key in fullview.keys():
        max_r = max(max_r, key[0])
        min_r = min(min_r, key[0])
        max_c = max(max_c, key[1])
        min_c = min(min_c, key[1])

    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            if (r, c) in fullview:
                print(fullview.get((r, c)), end="")
            else:
                print(".", end="")

        print()
    print()


def propogate_signal(sc, sr, bc, br):
    dist = abs(sc - bc) + abs(sr - br)

    r = target_row
    for c in range(dist - abs(target_row - sr) + 1):
        scan_view.update({(r, sc + c): "#", (r, sc - c): "#"})


for i, line in enumerate(open(0).read().splitlines()):
    print(i)
    sc, sr, bc, br = [int(x) for x in re.findall("(?:-)?\d+", line)]
    propogate_signal(sc, sr, bc, br)
    sigs_beacs.update({(sr, sc): "S", (br, bc): "B"})


fullview = scan_view | sigs_beacs

for pos in scan_view:
    if pos not in sigs_beacs:
        score_1 += 1

print(f"Part 1: {score_1}")
# print_board()
