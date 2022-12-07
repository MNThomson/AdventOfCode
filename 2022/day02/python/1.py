#!/usr/bin/env python3

"""
A: Rock,
B: Paper,
C: Scissors

Pt 1:
X: Rock,
Y: Paper,
Z: Scissors

Pt 2:
X: lose,
Y: draw,
Z: win
"""

part1_val = [
    [4, 8, 3],
    [1, 5, 9],
    [7, 2, 6]
]

part2_val = [
    [3, 4, 8],
    [1, 5, 9],
    [2, 6, 7]
]

with open("../input.txt") as file:
    data = file.readlines()

    part1, part2 = 0, 0

    for game in data:
        [elf, me] = game.split(" ", 2)
        elf, me = ord(elf) - ord("A"), ord(me.rstrip()) - ord("X")

        part1 += part1_val[elf][me]
        part2 += part2_val[elf][me]

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
