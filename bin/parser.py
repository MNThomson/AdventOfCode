#!/usr/bin/python3

import re

scoreboard = "| Day |   | Part 1: Time | Rank |   | Part 2: Time | Rank |\n"
scoreboard += "| --- | - | ------------ | ---: | - | ------------ | ---: |\n"

with open("scoreboard.txt") as file:
    for line in file.read().splitlines()[2::][::-1]:
        line = re.sub(" +", " ", line.lstrip())
        day, time1, rank1, score1, time2, rank2, score2 = line.split(" ")
        rank1, rank2 = "{:,}".format(int(rank1)), "{:,}".format(int(rank2))
        scoreboard += (
            f"| **{day}** | | _{time1}_ | `{rank1}` | | _{time2}_ | `{rank2}` |\n"
        )

print(scoreboard)
