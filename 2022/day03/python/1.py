#!/usr/bin/env python3


def score(st: str):
    if st.isupper():
        return ord(st) - ord("A") + 27
    else:
        return ord(st) - ord("a") + 1


with open("../input.txt") as file:
    data = file.read().splitlines()
    score_1, score_2 = 0, 0

    for i, pack in enumerate(data):
        l = len(pack) // 2
        left = pack[:l]
        right = pack[l:]
        score_1 += score((set(left) & set(right)).pop())

        if i % 3 == 0:
            score_2 += score((set(data[i]) & set(data[i + 1]) & set(data[i + 2])).pop())

    print(f"Part 1: {score_1}")
    print(f"Part 2: {score_2}")
