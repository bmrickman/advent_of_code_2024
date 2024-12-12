with open("./day10/input.txt", "r") as f:
    data = [[int(l) for l in line] for line in f.read().splitlines()]


def cell_in_data(i, j):
    return i in range(len(data)) and j in range(len(data[0]))


def distinct_trails(i: int, j: int, expected_val: int) -> list[tuple[int, int]]:
    if not cell_in_data(i, j):
        return 0
    elif data[i][j] != expected_val:
        return 0
    elif data[i][j] == 9:
        return 1
    else:
        return (
            distinct_trails(i, j + 1, expected_val + 1)
            + distinct_trails(i, j - 1, expected_val + 1)
            + distinct_trails(i + 1, j, expected_val + 1)
            + distinct_trails(i - 1, j, expected_val + 1)
        )


map_score = 0
for i, row in enumerate(data):
    for j, cell in enumerate(row):
        if cell == 0:
            map_score += distinct_trails(i, j, 0)


print(map_score)
