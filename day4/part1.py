import numpy as np
import itertools


def count_xmas(matrix: np.array):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            _is = [list(reversed(range(i - 3, i + 1))), [i] * 4, list(range(i, i + 4))]
            _js = [list(reversed(range(j - 3, j + 1))), [j] * 4, list(range(j, j + 4))]

            for _is, _js in list(itertools.product(_is, _js)):
                if (
                    min(_is) >= 0
                    and min(_js) >= 0
                    and max(_is) < len(matrix)
                    and max(_js) < len(matrix[0])
                    and "".join(matrix[_is, _js]) == "XMAS"
                ):
                    count += 1
    return count


assert count_xmas(np.array([["X", "M", "A", "S"]])) == 1
assert count_xmas(np.array([["S", "A", "M", "X"]])) == 1
assert count_xmas(np.array([["X"], ["M"], ["A"], ["S"]])) == 1
assert count_xmas(np.array([["S"], ["A"], ["M"], ["X"]])) == 1


with open("./day4/input.txt", "r") as f:
    data = f.read().splitlines()
    data = [list(row) for row in data]
    matrix = np.array(data)
print(count_xmas(matrix))
