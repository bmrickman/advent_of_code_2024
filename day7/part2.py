import operator
import itertools


def elephant(left, right):
    return int(str(left) + str(right))


base_ops = (operator.add, operator.mul, elephant)

with open("./day7/input.txt", "r") as f:
    rows = f.read().splitlines()
    rows = [row.split(" ") for row in rows]
    for i, row in enumerate(rows):
        rows[i][0] = row[0][:-1]
        rows[i] = [int(v) for v in row]


_count = 0
for row in rows:
    # create list of possible ops
    nops = len(row) - 2
    possible_op_combs = list(itertools.product(*(base_ops for _ in range(nops))))
    for ops in possible_op_combs:
        tot = row[1]
        for i, operand in enumerate(row[2:]):
            tot = ops[i](tot, operand)
        if tot == row[0]:
            _count += tot
            break

print(_count)

# 337
