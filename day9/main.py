
def move_knot(head, tail):
    hx, hy = head
    tx, ty = tail
    dx = hx - tx
    dy = hy - ty

    if (abs(dx) == 2) or (abs(dy) == 2):
        tx += (dx != 0) - (dx < 0) * 2
        ty += (dy != 0) - (dy < 0) * 2
    return (tx, ty)


def simulate_rope(steps, length=10):
    knots = [(0, 0)] * length
    tail_positions = set([knots[-1]])

    for step in steps:
        knots[0] = (knots[0][0] + step[0], knots[0][1] + step[1])
        for i in range(1, len(knots)):
            knots[i] = move_knot(knots[i-1], knots[i])
        tail_positions.add(knots[-1])

    return len(tail_positions)


with open("day9/input.txt") as fp:
    lines = [line.strip() for line in fp.readlines()]

steps = []
directions = {
    "U": [0, 1],
    "D": [0, -1],
    "R": [1, 0],
    "L": [-1, 0],
}

for line in lines:
    d, c = line.split()
    for i in range(int(c)):
        steps.append(directions[d])


print("q1:", simulate_rope(steps, length=2))
print("q2:", simulate_rope(steps, length=10))
