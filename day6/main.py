with open("day6/input.txt") as fp:
    line = fp.readlines()[0].strip()

i = 0
while len(line[i:i+4]) != len(set(line[i:i+4])):
    i += 1
print("part 1:", i + 4)

i = 0
while len(line[i:i+14]) != len(set(line[i:i+14])):
    i += 1
print("part 2:", i + 14)
