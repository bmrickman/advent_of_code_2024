with open("./day11/input.txt", "r") as f:
    data = [int(char) for char in f.read().split()]

nblinks = 25

old_data = data
new_data = []
for _ in range(nblinks):
    for num in old_data:
        if num == 0:
            new_data.append(num + 1)
        elif len(str(num)) % 2 == 0:
            ndigits = len(str(num))
            new_data.append(int(str(num)[: ndigits // 2]))
            new_data.append(int(str(num)[ndigits // 2 :]))
        else:
            new_data.append(num * 2024)
    old_data = new_data
    new_data = []

print(len(old_data))
