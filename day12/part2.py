import numpy as np
from collections import defaultdict, Counter


def rotate_vector_clockwise(vec, nrotations):
    rotation_matrix = np.array([[0, 1], [-1, 0]])
    for i in range(nrotations):
        vec = np.dot(rotation_matrix, vec)
    return vec


def index_in_matrix(matrix: tuple, index: tuple):
    index = np.array(index)
    return (index >= 0).all() and (index < matrix.shape).all()


with open("day12/input.txt", "r") as f:
    data = f.read().splitlines()
    data = [[cell for cell in row] for row in data]
    data = np.array(data)

next_plot_id = 0
plot_ids_matrix = np.full((len(data), len(data[0])), -1)


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
        return (
            [(i, j)]
            + get_cells_in_plot(i + 1, j, key)
            + get_cells_in_plot(i - 1, j, key)
            + get_cells_in_plot(i, j + 1, key)
            + get_cells_in_plot(i, j - 1, key)
        )


def count_corners(i, j):
    corners = 0
    directions = ((1, 0), (0, 1), (1, 1))
    comparisons = (
        directions,
        (rotate_vector_clockwise(dir, 1) for dir in directions),
        (rotate_vector_clockwise(dir, 2) for dir in directions),
        (rotate_vector_clockwise(dir, 3) for dir in directions),
    )
    for dir1, dir2, dir3 in comparisons:
        a = plot_ids_matrix[i, j]
        try:
            ind = np.array((i, j)) + dir1
            assert all(ind >= 0)
            b = plot_ids_matrix[*ind]
        except:
            b = -10
        try:
            ind = np.array((i, j)) + dir2
            assert all(ind >= 0)
            c = plot_ids_matrix[*ind]
        except:
            c = -11
        try:
            ind = np.array((i, j)) + dir3
            assert all(ind >= 0)
            d = plot_ids_matrix[*ind]
        except:
            d = -12
        if (a == b == c) and a != d:
            corners += 1
        elif a != b and a != c:
            corners += 1
    return corners


plot_ids_to_cells = {}
for i in range(len(data)):
    for j in range(len(data[0])):
        # skip squares that area already part of a shape
        if plot_ids_matrix[i, j] != -1:
            pass
        else:
            # get all squares that are part of the new shape
            cells = get_cells_in_plot(i, j, data[i, j])
            # calculate the area and ncorners (which is == to nsides for a shape)
            plot_ids_to_cells[next_plot_id] = cells
            next_plot_id += 1

total = 0
for plot_id, cells in plot_ids_to_cells.items():
    nsides = ncorners = sum(count_corners(*cell) for cell in cells)
    area = len(cells)
    total += nsides * area
print(total)
