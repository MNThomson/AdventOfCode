#!/usr/bin/env python3


def visible_left(data, i, j):
    val = 0
    for jx in range(j - 1, -1, -1):
        val += 1
        if data[i][jx] >= data[i][j]:
            break
    return val


def visible_right(data, i, j):
    val = 0
    for jx in range(j + 1, len(data[i])):
        val += 1
        if data[i][jx] >= data[i][j]:
            break
    return val


def visible_up(data, i, j):
    val = 0
    for ix in range(i - 1, -1, -1):
        val += 1
        if data[ix][j] >= data[i][j]:
            break
    return val


def visible_down(data, i, j):
    val = 0
    for ix in range(i + 1, len(data)):
        val += 1
        if data[ix][j] >= data[i][j]:
            break
    return val


def is_visible(data, i, j):
    return (
        visible_left(data, i, j)
        * visible_right(data, i, j)
        * visible_up(data, i, j)
        * visible_down(data, i, j)
    )


with open("/home/mthomson/proj/AdventOfCode/2022/day08/input.txt") as file:
    data = file.read().splitlines()
    score_2 = 0

    for i, line in enumerate(data):
        data[i] = [int(j) for j in line]

    for i, line in enumerate(data):
        for j, tree in enumerate(line):
            score_2 = max(score_2, is_visible(data, i, j))

    print(f"Part 2: {score_2}")
