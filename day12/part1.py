import numpy as np
from collections import defaultdict


def index_in_matrix(matrix: tuple, index: tuple):
    index = np.array(index)
    return (index >= 0).all() and (index < matrix.shape).all()


with open("day12/input.txt", "r") as f:
    data = f.read().splitlines()
    data = [[cell for cell in row] for row in data]
    data = np.array(data)

next_plot_id = 0
plot_ids_matrix = np.full((len(data), len(data[0])), -1)
plot_ids_to_area = defaultdict(lambda: 0)
plot_ids_to_perimeter = defaultdict(lambda: 0)


def get_cells_in_plot(i, j, key):
    if not index_in_matrix(data, (i, j)):
        return []
    if data[i, j] != key:  # This cell is not part of this shape
        return []
    elif (
        plot_ids_matrix[i, j] != -1
    ):  # This cell has already been accounted for in some shape
        return []
    else:
        global next_plot_id
        plot_ids_matrix[i, j] = next_plot_id
        next_plot_id += 1
        return (
            [(i, j)]
            + get_cells_in_plot(i + 1, j, key)
            + get_cells_in_plot(i - 1, j, key)
            + get_cells_in_plot(i, j + 1, key)
            + get_cells_in_plot(i, j - 1, key)
        )


def get_cell_perimiter(cells: tuple[int, int], key):
    tot = 0
    for i, j in cells:
        for adjacent_index in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if not index_in_matrix(data, adjacent_index):
                tot += 1
            elif data[adjacent_index] == key:
                pass
            else:
                tot += 1
    return tot


tot_cost = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if plot_ids_matrix[i, j] != -1:
            pass
        else:
            cells = get_cells_in_plot(i, j, data[i, j])
            perimiter = get_cell_perimiter(cells, data[i, j])
            tot_cost += len(cells) * perimiter

print(tot_cost)
