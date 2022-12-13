#!/usr/bin/env python3


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


i2 = 1
i6 = 2

for line in list(map(eval, open(0).read().split())):
    if score(line, [[2]]) < 0:
        i2 += 1
        i6 += 1
    elif score(line, [[6]]) < 0:
        i6 += 1


print(f"Part 2: {i2 * i6}")
