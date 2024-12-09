import numpy as np
from copy import copy

direction_char_to_vector = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
direction_vector_to_char = {v: k for k, v in direction_char_to_vector.items()}


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


def get_path(startpos: tuple[int, int], startdir: tuple[int, int], data: np.array):
    curpos, curdir = startpos, startdir
    while True:
        newpos = tuple(np.array(curpos) + np.array(curdir))
        if not (  # check if we are about to leave the matrix
            newpos[0] >= 0
            and newpos[1] >= 0
            and newpos[0] < len(data)
            and newpos[1] < len(data[0])
        ):
            break
        yield (curpos, curdir)  # left inclusive
        if data[newpos] in ("#", "O"):
            curdir = rotate(curdir)
        else:
            curpos = newpos


if __name__ == "__main__":
    # load the data
    with open("./day6/input.txt", "r") as f:
        data = f.read().splitlines()
        data = np.array([list(row) for row in data])
    # get initial position
    curpos = None
    curdir = None
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell in ("^", "v", ">", "<"):
                startpos = (i, j)
                startdir = direction_char_to_vector[cell]

    ## CORE LOGIC ## ##
    cycle_positions = []
    # for each position in the path that we might take
    for pos, dir in get_path(startpos, startdir, data):
        data[pos] = direction_vector_to_char(
            dir
        )  # mark the current position and direction
        curpos, curdir = pos, dir
        #  we imagine there is a blockage and follow the path we would then take
        potential_block_id = tuple(np.array(curpos) + np.array(curdir))
        cdata = copy(data)
        try:
            cdata[potential_block_id] = "O"
        except IndexError:
            break
        path_cache = {}
        for pos, dir in get_path(curpos, curdir, cdata):
            cdata[pos] = direction_vector_to_char(dir)
            # if we eventaully end up hitting a path we've already walked
            if (pos, dir) in path_cache:
                # store the cycle position
                cycle_positions.append(potential_block_id)
                print(cdata)
                print("\n\n\n\n")
                break
            path_cache[(pos, dir)] = None


cycle_positions = [pos for pos in cycle_positions if pos != startpos]
print(len(set(cycle_positions)))
