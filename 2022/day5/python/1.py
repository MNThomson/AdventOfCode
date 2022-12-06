#!/usr/bin/env python3


def setup_state(crates, num_rows):
    state = [[] for x in range(len(crates))]

    for i, line in enumerate(crates[:-1]):
        for j in range(num_rows):
            if crates[i][j * 4 + 1] != " ":
                state[j].append(crates[i][j * 4 + 1])
    return state


def handle_move_1(state, move_text):
    _, num, _, frm, _, to = move_text.split(" ")
    num, frm, to = int(num), int(frm) - 1, int(to) - 1

    for _ in range(num):
        state[to].insert(0, state[frm].pop(0))
    return state


def handle_move_2(state, move_text):
    _, num, _, frm, _, to = move_text.split(" ")
    num, frm, to = int(num), int(frm) - 1, int(to) - 1

    for i in range(num):
        state[to].insert(i, state[frm].pop(0))
    return state


def score_state(state):
    outstr = ""
    for line in state:
        outstr += line[0]

    return outstr


with open("../input.txt") as file:
    score_1, score_2 = 0, 0

    [crates, instructions] = file.read().split("\n\n", 2)
    crates, instructions = crates.splitlines(), instructions.splitlines()
    num_rows = (len(crates[-1]) + 1) // 4

    state_1, state_2 = setup_state(crates, num_rows), setup_state(crates, num_rows)

    for instr in instructions:
        state_1 = handle_move_1(state_1, instr)
        state_2 = handle_move_2(state_2, instr)

    score_1 = score_state(state_1)
    score_2 = score_state(state_2)

    print(f"Part 1: {score_1}")
    print(f"Part 2: {score_2}")
