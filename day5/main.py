import re
import numpy as np

with open("day5/input.txt") as fp:
    lines =  [l.strip() for l in fp.readlines()]

moves = []
stacks_height = lines.index("") - 1
instruction_start = lines.index("") + 1

for i in range(instruction_start, len(lines)):
    a, b, c = map(int, re.search(r"move (\d+) from (\d+) to (\d+)", lines[i]).groups())
    moves.append([a, b-1, c-1])

stacks = [[] for _ in range(1 + len(lines[stacks_height])//4)]

for l in lines[0:stacks_height]:
    for i, c in enumerate(l[1::4]):
        if c != " ":
            stacks[i] = [c] + stacks[i] 

for c, frm, to in moves:
    for _ in range(c):
        stacks[to].append(stacks[frm].pop())

print("part 1:", "".join([s[-1] for s in stacks if len(s) > 0]))


stacks = [[] for _ in range(1 + len(lines[stacks_height])//4)]

for l in lines[0:stacks_height]:
    for i, c in enumerate(l[1::4]):
        if c != " ":
            stacks[i] = [c] + stacks[i]

for c, frm, to in moves:
    stacks[to] += stacks[frm][-c:]
    stacks[frm] = stacks[frm][:-c]

print("part 2:", "".join([s[-1] for s in stacks if len(s) > 0]))
