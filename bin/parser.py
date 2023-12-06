#!/usr/bin/python3

import re

scoreboard_str =  "| Day |   | Part 1: Time | Rank (Percentile) |   | Part 2: Time | Rank (Percentile) |\n"
scoreboard_str += "| --- | - | ------------ | ----------------: | - | ------------ | ----------------: |\n"

with open("scoreboard.txt") as file:
    scoreboard = file.read().splitlines()[2::][::-1]

with open("stats.txt") as file:
    stats = file.read().splitlines()[::-1]


for score_line, stats_line in zip(scoreboard, stats):
    score_line, stats_line = re.sub(" +", " ", score_line.lstrip()), re.sub(
        " +", " ", stats_line.lstrip()
    )

    day, time1, rank1, score1, time2, rank2, score2 = score_line.split(" ")
    rank1_fmt, rank2_fmt = "{:,}".format(int(rank1)), "{:,}".format(int(rank2))

    _, gold_num, silver_num, _ = stats_line.split(" ", 3)
    total_attempted = int(gold_num) + int(silver_num)

    percentile1 = (total_attempted - int(rank1)) * 100 // total_attempted
    percentile2 = (int(gold_num) - int(rank2)) * 100 // int(gold_num)

    scoreboard_str += f"| **{day}** | | _{time1}_ | `{rank1_fmt}` ({percentile1}%) |  | _{time2}_ | `{rank2_fmt}` ({percentile2}%) |\n"

print(scoreboard_str)
