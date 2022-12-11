#!/usr/bin/env python3

from typing import Any, List


class Monkey:
    def __init__(self, txt):
        parsed = txt.splitlines()
        self.id: int = parsed[0].split("Monkey ", 2)[1].split(":", 2)[0]
        self.items = list(map(int, parsed[1].split(": ", 2)[1].split(", ")))
        self.operation_type = (
            "square"
            if parsed[2].split(" ")[-1] == "old"
            else "mul"
            if parsed[2].split("Operation: new = ", 2)[1].split(" ", 2)[1] == "*"
            else "add"
            if parsed[2].split("Operation: new = ", 2)[1].split(" ", 2)[1] == "+"
            else "Bad"
        )

        self.operation_val = (
            int(parsed[2].split(" ")[-1]) if self.operation_type != "square" else 0
        )

        self.test = int(parsed[3].split("divisible by ", 2)[1])
        self.true = int(parsed[4].split("If true: throw to monkey ", 2)[1])
        self.false = int(parsed[5].split("If false: throw to monkey ", 2)[1])
        self.score = 0

    def __str__(self):
        return ", ".join(list(map(str, self.items)))

    def do_operation(self, item: int):
        if self.operation_type == "mul":
            return item * self.operation_val
        elif self.operation_type == "add":
            return item + self.operation_val
        elif self.operation_type == "square":
            return item * item

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
            item = self.do_operation(item)
            item = item // 3
            throw_to = self.throw_item(item)
            monkeys[throw_to].catch_item(item)

        self.items = []


monkeys: List[Monkey] = []


for monkey in open(0).read().split("\n\n"):
    monkeys.append(Monkey(monkey))
    continue

for _ in range(20):
    for monkey in monkeys:
        monkey.take_turn(monkeys)


def score_1(monkeys):
    score = [int(monkey.score) for monkey in monkeys]
    top = max(score)
    score.remove(top)
    sec = max(score)
    print(score, top, sec)
    return top * sec


print(f"Part 1: {score_1(monkeys)}")
