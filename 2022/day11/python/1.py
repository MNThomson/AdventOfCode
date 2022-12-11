#!/usr/bin/env python3

from math import lcm
from typing import Any, List


class Monkey:
    def __init__(self, txt, div_3):
        parsed = txt.splitlines()
        self.div_3 = div_3
        self.id: int = parsed[0].split("Monkey ", 2)[1].split(":", 2)[0]
        self.items = list(map(int, parsed[1].split(": ", 2)[1].split(", ")))
        self.operation = eval("lambda old:" + parsed[2].split("=")[1])
        self.test = int(parsed[3].split("divisible by ", 2)[1])
        self.true = int(parsed[4].split("If true: throw to monkey ", 2)[1])
        self.false = int(parsed[5].split("If false: throw to monkey ", 2)[1])
        self.score = 0

    def __str__(self):
        return ", ".join(list(map(str, self.items)))

    def catch_item(self, item):
        self.items.append(item)

    def throw_item(self, item: int):
        if item % self.test == 0:
            return self.true
        else:
            return self.false

    def take_turn(self, monkeys: List[Any]):
        for item in self.items:
            self.score += 1
            item = self.operation(item)

            if self.div_3:
                item = item // 3
            else:
                item %= lcm_div

            throw_to = self.throw_item(item)
            monkeys[throw_to].catch_item(item)

        self.items = []


def score(monkeys):
    score = [int(monkey.score) for monkey in monkeys]
    sort = sorted(score, reverse=True)
    return sort[0] * sort[1]


monkeys_1: List[Monkey] = []
monkeys_2: List[Monkey] = []

for monkey in open(0).read().split("\n\n"):
    monkeys_1.append(Monkey(monkey, True))
    monkeys_2.append(Monkey(monkey, False))
    continue

lcm_div = 1

for monkey in monkeys_1:
    lcm_div = lcm(lcm_div, monkey.test)

for _ in range(20):
    for monkey in monkeys_1:
        monkey.take_turn(monkeys_1)

for _ in range(10_000):
    for monkey in monkeys_2:
        monkey.take_turn(monkeys_2)

print(f"Part 1: {score(monkeys_1)}")
print(f"Part 2: {score(monkeys_2)}")
