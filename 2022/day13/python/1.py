#!/usr/bin/env python3

from pprint import pprint
from typing import Set

score_1 = 0


def score(l, r) -> bool:
    if type(l) == int:
        if type(r) == int:
            return l - r
        else:
            return score([l], r)
    else:
        if type(r) == int:
            return score(l, [r])

    for ll, rr in zip(l, r):
        ret = score(ll, rr)
        if ret:
            return ret

    return len(l) - len(r)


for i, line in enumerate(open(0).read().split("\n\n")):
    l, r = line.split("\n", 2)
    l, r = eval(l), eval(r)
    print("Starting:", l, r)

    if score(l, r) < 0:
        score_1 += i + 1

    print(f"Score: {score_1}")


print(f"Part 1: {score_1}")
