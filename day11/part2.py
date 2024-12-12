from functools import lru_cache

with open("./day11/input.txt", "r") as f:
    data = [int(char) for char in f.read().split()]

nblinks = 75


@lru_cache(maxsize=None)
def get_final_length(num, blinks_left):
    if blinks_left == 0:
        return 1
    elif num == 0:
        return get_final_length(num + 1, blinks_left - 1)
    elif len(str(num)) % 2 == 0:
        ndigits = len(str(num))
        return get_final_length(
            int(str(num)[: ndigits // 2]), blinks_left - 1
        ) + get_final_length(int(str(num)[ndigits // 2 :]), blinks_left - 1)
    else:
        return get_final_length(num * 2024, blinks_left - 1)


print(sum(get_final_length(num, nblinks) for num in data))
