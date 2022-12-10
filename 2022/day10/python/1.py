#!/usr/bin/env python3

cycles = [1]

for instr in open(0).read().splitlines():
    cycles.append(cycles[-1])

    if instr == "noop":
        continue

    num = int(instr.split()[1])
    cycles.append(cycles[-1] + num)


score_1 = lambda cycles: sum([i * s + s for i, s in list(enumerate(cycles))[19::40]])


def score_2(cycles):
    s = ""
    for i, p in enumerate(cycles[:-1]):
        i = i % 40
        if i == 0:
            s += "\n"

        if abs(i - p) <= 1:
            s += "#"
        else:
            s += "."
    return s


print(f"Part 1: {score_1(cycles)}")
print(f"Part 2: {score_2(cycles)}")
