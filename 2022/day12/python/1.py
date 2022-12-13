#!/usr/bin/env python3

from collections import deque

terrain = []

for row, line in enumerate(open(0).read().splitlines()):
    terrain.append([])

    for col, char in enumerate(line):
        val = None
        if char == "S":
            val = 0
            sr = row
            sc = col
        elif char == "E":
            val = 25
            dr = row
            dc = col
        else:
            val = ord(char) - ord("a")

        terrain[row].append(val)

queue = deque()
queue.append((0, sr, sc))

visited = {(sr, sc)}

while len(queue) > 0:
    steps_taken, row, col = queue.popleft()
    for move_r, move_c in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
        if move_r < 0 or move_c < 0 or move_r >= len(terrain) or move_c >= len(terrain[0]):
            continue

        if (move_r, move_c) in visited:
            continue

        if terrain[move_r][move_c] - terrain[row][col] > 1:
            continue

        if move_r == dr and move_c == dc:
            print(f"Part 1: {steps_taken + 1}")
            exit(0)

        visited.add((move_r, move_c))
        queue.append((steps_taken + 1, move_r, move_c))
