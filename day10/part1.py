with open("./day10/input.txt", "r") as f:
    data = [[int(l) for l in line] for line in f.read().splitlines()]


def cell_in_data(i, j):
    return i in range(len(data)) and j in range(len(data[0]))


def accessible_trail_tops(i: int, j: int, expected_val: int) -> list[tuple[int, int]]:
    if not cell_in_data(i, j):
        return []
    elif data[i][j] != expected_val:
        return []
    elif data[i][j] == 9:
        return [(i, j)]
    else:
        return (
            accessible_trail_tops(i, j + 1, expected_val + 1)
            + accessible_trail_tops(i, j - 1, expected_val + 1)
            + accessible_trail_tops(i + 1, j, expected_val + 1)
            + accessible_trail_tops(i - 1, j, expected_val + 1)
        )


map_score = 0
for i, row in enumerate(data):
    for j, cell in enumerate(row):
        if cell == 0:
            map_score += len(set(accessible_trail_tops(i, j, 0)))


print(map_score)
