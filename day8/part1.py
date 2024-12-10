import numpy as np
from collections import defaultdict
import itertools

with open("./day8/input.txt", "r") as f:
    data = f.read().splitlines()
    data = [[char for char in row] for row in data]
    data = np.array(data)


antennas = defaultdict(lambda: [])
for i, row in enumerate(data):
    for j, cell in enumerate(row):
        if cell != ".":
            antennas[cell].append(np.array((i, j)))

antinodes = {}
for signal in antennas.keys():
    pairs = list(itertools.product(antennas[signal], antennas[signal]))
    for pair in pairs:
        if pair[0] is pair[1]:
            pass
        else:
            p1 = pair[0] + (pair[0] - pair[1])
            p2 = pair[1] + (pair[1] - pair[0])
            for p in (p1, p2):
                if p[0] >= 0 and p[1] >= 0 and p[0] < len(data) and p[1] < len(data[0]):
                    antinodes[tuple(p)] = None


print(len(antinodes.keys()))
