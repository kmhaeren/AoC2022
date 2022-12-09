import numpy as np

with open("day2/input.txt") as fp:
    p0, p1 = np.array([[ord(l) - ord(c) for l, c in zip(line.strip().split(" "), ("A", "X"))]
                       for line in fp.readlines()]).T

print("q1:", sum(p1 + 1 + 3 * (2 - (p0 - p1 + 1) % 3)))
print("q2:", sum((p0 - 1 + p1) % 3 + 1 + 3 * p1))
