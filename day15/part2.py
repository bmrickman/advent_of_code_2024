import numpy as np

with open("./day15/input.txt", "r") as f:
    data = f.read()
    data = (
        data.replace(".", "..").replace("#", "##").replace("O", "[]").replace("@", ".")
    )
    data = data.splitlines()
    for i, line in enumerate(data):
        if line == "":
            break
    map = np.array([[char for char in row] for row in data[:i]])
    instructions = data[i + 1 :]
    instructions = "".join(instructions)


def vectorize(direction: str):
    if direction == "<":
        return np.array((0, -1))
    elif direction == "^":
        return np.array((-1, 0))
    elif direction == ">":
        return np.array((0, 1))
    elif direction == "v":
        return np.array((1, 0))


def shift_char(pos: np.array, direction: np.array):
    # if we are moving into a wall, we are unable to shift
    if map[*pos + direction] == "#":
        return False
    # if we are trying to walk to an open space, just complete the shift
    elif map[*pos + direction] == ".":
        map[*pos + direction] = map[*pos]
        map[*pos] = "."
        return True
    # if there is a box, we first try and shift the box over
    elif map[*pos + direction] in ("[", "]") and direction in (
        np.array((0, -1)),
        np.array((0, 1)),
    ):
        if shift_char(pos + direction, direction):
            map[*pos + direction] = map[*pos]
            map[*pos] = "."
            return True
        else:
            return False
    elif map[*pos + direction] in ("[", "]") and direction in (
        np.array((1, 0)),
        np.array((-1, 0)),
    ):
        if map[*pos + direction] == "[":
            if shift_char()
        elif map[*pos + direction] == "]":
            pass


for i, row in enumerate(map):
    for j, cell in enumerate(row):
        if cell == "@":
            pos = np.array((i, j))

for i, direction in enumerate(instructions):
    vector_dir = vectorize(direction)
    if shift_char(pos, vector_dir):
        pos = pos + vector_dir

total = 0
for i, row in enumerate(map):
    for j, cell in enumerate(row):
        if cell == "O":
            total += 100 * i + j

print(total)
