#!/usr/bin/env python3


def contains(l, r):
    [l1, l2], [r1, r2] = l.split("-", 2), r.split("-", 2)
    l1, l2, r1, r2 = int(l1), int(l2), int(r1), int(r2)

    if (l1 >= r1 and l2 <= r2):
        return True
    return False


def overlaps(l, r):
    [l1, l2], [r1, r2] = l.split("-", 2), r.split("-", 2)
    l1, l2, r1, r2 = int(l1), int(l2), int(r1), int(r2)

    if (l1 <= r1 and r1 <= l2):
        return True
    return False


with open("../input.txt") as file:
    data = file.read().splitlines()
    score_1, score_2 = 0, 0

    for i, line in enumerate(data):
        l, r = line.split(",")
        if contains(l, r) or contains(r, l):
            score_1 += 1
        if overlaps(l, r) or overlaps(r, l):
            score_2 += 1

    print(f"Part 1: {score_1}")
    print(f"Part 2: {score_2}")
