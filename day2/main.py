import numpy as np

with open("day2/input.txt") as fp:
    p = np.array([[ord(l) - ord(c) for l,c in zip(line.strip().split(" "), ("A", "X"))] for line in fp.readlines()])

print("q1:", sum(p[:, 1] + 1 + 3 * (2 - (p[:, 0]- p[:, 1] + 1) % 3) ))
print("q2:", sum((p[:, 0] - 1 + p[: ,1]) % 3 + 1 + 3 * p[: ,1]))

