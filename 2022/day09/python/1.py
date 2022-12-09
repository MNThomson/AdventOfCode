#!/usr/bin/env python3

rope = [0] * 10
visited = [set([v]) for v in rope]
sign = lambda input: (input > 0) - (input < 0)

for move in open("../input.txt"):
    direction, num = move.split()
    num = int(num)

    movement = {"D": 1j, "U": -1j, "L": +1, "R": -1}

    for _ in range(num):
        rope[0] += movement[direction]

        for i in range(1, len(rope)):
            distance = rope[i - 1] - rope[i]
            if abs(distance) >= 2:
                rope[i] += complex(sign(distance.real), sign(distance.imag))
                visited[i].add(rope[i])

print(f"Part 1: {len(visited[1])}")
print(f"Part 2: {len(visited[9])}")
