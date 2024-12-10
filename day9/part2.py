from collections import namedtuple
from dataclasses import dataclass


@dataclass
class SymFile:
    val: int
    length: int


with open("./day9/input.txt", "r") as f:
    disk = f.read()
    disk = [int(char) for char in disk]

# a less performant version, because this is too complicated
sym_disk = [
    SymFile(i // 2, f) if i % 2 == 0 else SymFile(".", f) for i, f in enumerate(disk)
]
new_disk = []

for i, left_file in enumerate(sym_disk):
    if left_file.val != ".":
        new_disk.extend([left_file.val] * left_file.length)
        left_file.val = "X"
    elif left_file.val == "X":
        pass
    else:
        free_space = left_file.length
        for right_file in reversed(sym_disk[i:]):
            if right_file.val not in (".", "X") and right_file.length <= free_space:
                free_space = free_space - right_file.length
                new_disk.extend([right_file.val] * right_file.length)
                right_file.val = "X"
        new_disk.extend(["."] * free_space)


print(sum([x * i for i, x in enumerate(new_disk) if x not in (".", "X")]))
