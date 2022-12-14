#!/usr/bin/env python3

import math

score_1 = 0
terrain = {}

lowest_r = 0


def print_board():
    max_r = min_r = 0
    max_c = min_c = 500
    for key in terrain.keys():
        max_r = max(max_r, key[0])
        min_r = min(min_r, key[0])
        max_c = max(max_c, key[1])
        min_c = min(min_c, key[1])

    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            if (r, c) in terrain:
                print(terrain.get((r, c)), end="")
            else:
                print(".", end="")

        print()
    print()


def simulate():
    pos = (0, 500)
    for i in range(lowest_r + 1):
        for j, loc in enumerate(
            [
                (pos[0] + 1, pos[1]),
                (pos[0] + 1, pos[1] - 1),
                (pos[0] + 1, pos[1] + 1),
            ]
        ):
            if loc in terrain:
                if j == 2:
                    terrain.update({pos: "o"})
                continue
            pos = loc

            if i == lowest_r:
                return False
            break

    return True


for line in open(0).read().splitlines():
    verts = line.split(" -> ")
    for i in range(len(verts) - 1):
        l, r = (eval(verts[i])), (eval(verts[i + 1]))

        if l[0] != r[0]:
            for p in range(l[0], r[0], int(math.copysign(1, r[0] - l[0]))):
                terrain.update(
                    {
                        (
                            l[1],
                            p,
                        ): "#"
                    }
                )
            terrain.update({(l[1], r[0]): "#"})
        else:
            for p in range(l[1], r[1], int(math.copysign(1, r[1] - l[1]))):
                terrain.update({(p, r[0]): "#"})
            terrain.update({(r[1], l[0]): "#"})


for key in terrain.keys():
    lowest_r = max(lowest_r, key[0])


while simulate():
    score_1 += 1
    # print_board()
    continue


print(f"Part 1: {score_1}")
# print_board()
