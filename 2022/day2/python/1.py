#!/usr/bin/env python3

"""
A: Rock,
B: Paper,
C: Scissors

X: Rock,
Y: Paper, 
Z: Scissors
"""

score = [
    [4, 8, 3], 
    [1, 5, 9], 
    [7, 2, 6]
]


with open("../input.txt") as my_file:
    data = my_file.readlines()

    val = 0
    for game in data:
        [elf, me] = game.split(" ", 2)
        val += score[ord(elf) - 65][ord(me.rstrip()) - 88]

    print(f"Part 1: {val}")
