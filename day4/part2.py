import numpy as np


def count_x_mas(matrix: np.array):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            try:
                if i - 1 >= 0 and j - 1 >= 0:
                    word1 = "".join(matrix[(i - 1, i, i + 1), (j - 1, j, j + 1)])
                    word2 = "".join(matrix[(i - 1, i, i + 1), (j + 1, j, j - 1)])
                    if word1 in ("MAS", "SAM") and word2 in ("MAS", "SAM"):
                        count += 1
            except:
                pass
    return count


with open("./day4/input.txt", "r") as f:
    data = f.read().splitlines()
    data = [list(row) for row in data]
    matrix = np.array(data)
print(count_x_mas(matrix))
