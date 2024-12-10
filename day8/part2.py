import numpy as np
from collections import defaultdict
import itertools

with open("./day8/input.txt", "r") as f:
    data = f.read().splitlines()
    data = [[char for char in row] for row in data]
    data = np.array(data)


def index_in_matrix(ind, data):
    return ind[0] >= 0 and ind[1] >= 0 and ind[0] < len(data) and ind[1] < len(data[0])


antennas = defaultdict(lambda: [])
for i, row in enumerate(data):
    for j, cell in enumerate(row):
        if cell != ".":
            antennas[cell].append(np.array((i, j)))

antinodes = {}
for signal in antennas.keys():
    pairs = list(itertools.product(antennas[signal], antennas[signal]))
    pairs = [pair for pair in pairs if tuple(pair[0]) != tuple(pair[1])]
    for pair in pairs:
        point = pair[0]
        for vector in (pair[0] - pair[1], pair[1] - pair[0]):
            while index_in_matrix(point, data):
                antinodes[tuple(point)] = None
                point = point + vector


print(len(antinodes.keys()))
