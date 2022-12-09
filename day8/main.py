import numpy as np
from plotly import express as px
import plotly.graph_objects as go


with open("day8/input.txt") as fp:
    lines = [[int(ll) for ll in l.strip()] for l in fp.readlines()]

forest = np.array(lines)
w, h = forest.shape

visibility_grid = np.zeros_like(forest)
view_grid = np.ones_like(forest)

for _ in range(4):
    forest = np.rot90(forest)
    visibility_grid = np.rot90(visibility_grid)
    view_grid = np.rot90(view_grid)
    for i in range(w):
        current_max = -1
        for j in range(w):
            if forest[i, j] > current_max:
                visibility_grid[i, j] += 1
                current_max = forest[i, j]

            view = 1
            while ((view + j + 1) < w) and (forest[i, j] > forest[i, j + view]):
                view += 1
            view_grid[i, j] *= view

print("q1:", np.sum(np.sum(visibility_grid != 0)))
print("q2:", np.max(view_grid))
