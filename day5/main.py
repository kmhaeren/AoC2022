import re
import copy

with open("day5/input.txt") as fp:
    lines =  [l.strip() for l in fp.readlines()]

c = 0
stacks = []

while lines[c+1] != "":
    line = lines[c][1::4]
    stacks.extend([[] for _ in range(len(line) - len(stacks))])
    for s, l in zip(stacks, line):
        if l != " ":
            s.insert(0, l)
    c += 1

stacks2 = copy.deepcopy(stacks)

for line in lines[c+2:]:
    v, src, dst = map(int, re.search(r"move (\d+) from (\d+) to (\d+)", line).groups())
    for _ in range(v):
        stacks[dst-1].append(stacks[src-1].pop())
    
    stacks2[dst-1] += stacks2[src-1][-v:]
    stacks2[src-1] = stacks2[src-1][:-v]


print("part 1:", "".join([s[-1] for s in stacks if len(s) > 0]))
print("part 2:", "".join([s[-1] for s in stacks2 if len(s) > 0]))
