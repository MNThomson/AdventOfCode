#!/usr/bin/env python3

def _sum(str):
    str = str.split("\n")
    arr = list(map(int, arr))
    return sum(arr)


with open("../input.txt") as my_file:
    data = my_file.read().rstrip().split("\n\n")

    data = list(map(_sum, data))

    data = sorted(data, reverse=True)

    print(f"Part 1: {data[0]}")
    print(f"Part 2: {sum(data[:3])}")
