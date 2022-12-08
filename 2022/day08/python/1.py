#!/usr/bin/env python3


def visible_left(data, i, j):
    for jx in range(j):
        if data[i][jx] >= data[i][j]:
            return False
    return True


def visible_right(data, i, j):
    for jx in range(len(data[i]) - 1, j, -1):
        if data[i][jx] >= data[i][j]:
            return False
    return True


def visible_up(data, i, j):
    for ix in range(i):
        if data[ix][j] >= data[i][j]:
            return False
    return True


def visible_down(data, i, j):
    for ix in range(len(data) - 1, i, -1):
        if data[ix][j] >= data[i][j]:
            return False
    return True


def is_visible(data, i, j):
    return (
        visible_left(data, i, j)
        or visible_right(data, i, j)
        or visible_up(data, i, j)
        or visible_down(data, i, j)
    )


with open("../input.txt") as file:
    data = file.read().splitlines()
    score_1 = 0

    for i, line in enumerate(data):
        data[i] = [int(j) for j in line]

    for i, line in enumerate(data):
        for j, tree in enumerate(line):
            if is_visible(data, i, j):
                score_1 += 1

    print(f"Part 1: {score_1}")
