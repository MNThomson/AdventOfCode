#!/usr/bin/env python3


def find_marker(data, length):
    for i in range(len(data) - length):
        if len(set(data[i : i + length])) == length:
            return i + length


with open("../input.txt") as file:
    data = file.read().splitlines()[0]

    score_1 = find_marker(data, 4)
    score_2 = find_marker(data, 14)

    print(f"Part 1: {score_1}")
    print(f"Part 2: {score_2}")
