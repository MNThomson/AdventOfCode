#!/usr/bin/env python3


def update_pwd(pwd, cmd):
    if cmd == "/":
        return ["/"]

    if cmd == "..":
        return pwd[:-1]

    pwd.append(cmd)
    return pwd


def update_filesystem(files, pwd, out):
    cur_dir = files

    for dir in pwd:
        cur_dir = cur_dir[dir]

    for o in out:
        i, j = o.split(" ")
        if i == "dir":
            cur_dir.setdefault(j, {})
        else:
            cur_dir.setdefault(j, int(i))

    return files


def score_1(files):
    if type(files) == int:
        return (files, 0)

    size, answer = 0, 0

    for child in files.values():
        s, a = score_1(child)
        size += s
        answer += a

    if size <= 100000:
        answer += size

    return (size, answer)


def size(files):
    if type(files) == int:
        return files
    return sum(map(size, files.values()))


def score_2(files, max_size):
    answer = float("inf")
    if size(files) >= max_size:
        answer = size(files)

    for child in files.values():
        if type(child) == int:
            continue
        new_answer = score_2(child, max_size)
        answer = min(answer, new_answer)
    return answer


with open("../input.txt") as file:
    data = file.read().split("$ ")

    commands = [line.splitlines() for line in data][1:]
    pwd = ["/"]
    files = {"/": {}}

    for cmdline in commands:
        cmd = cmdline[0].split(" ")

        if cmd[0] == "cd":
            pwd = update_pwd(pwd, cmd[1])
            continue

        out = cmdline[1:]

        files = update_filesystem(files, pwd, out)

    print(f"Part 1: {score_1(files)[1]}")

    max_size = size(files) - 40_000_000
    print(f"Part 2: {score_2(files, max_size)}")
