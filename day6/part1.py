import numpy as np

with open("./day6/input.txt", "r") as f:
    data = f.read().splitlines()
    data = np.array([list(row) for row in data])


def vectorize_direction(direction: str) -> tuple[int, int]:
    if direction == ">":
        return (0, 1)
    elif direction == "<":
        return (0, -1)
    if direction == "^":
        return (-1, 0)
    if direction == "v":
        return (1, 0)
    raise Exception("You're probably using the wrong character set")


def rotate(direction: tuple[str, str]):
    if direction == (0, 1):  # right
        return (1, 0)
    elif direction == (1, 0):  # down
        return (0, -1)
    if direction == (0, -1):  # left
        return (-1, 0)
    if direction == (-1, 0):  # up
        return (0, 1)
    raise Exception("You're probably using the wrong character set")


allpos = {}
curpos = None
curdir = None
for i, row in enumerate(data):
    for j, cell in enumerate(row):
        if cell in ("^", "v", ">", "<"):
            curpos = (i, j)
            curdir = vectorize_direction(cell)
            allpos[curpos] = None

while True:
    newpos = tuple(np.array(curpos) + np.array(curdir))
    if not (  # check if we are about to leave the matrix
        newpos[0] >= 0
        and newpos[1] >= 0
        and newpos[0] < len(data)
        and newpos[1] < len(data[0])
    ):
        break
    if data[newpos] == "#":
        curdir = rotate(curdir)
    else:
        curpos = newpos
        allpos[curpos] = None
        data[curpos] = "X"

print(len(allpos.keys()))
