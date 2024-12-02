with open("./day1/input.txt", "r") as f:
    data = f.read().splitlines()

left_nums = []
right_nums = []
for line in data:
    l, r = line.split()
    left_nums.append(l)
    right_nums.append(r)

tot = 0
for l in left_nums:
    tot += right_nums.count(l) * int(l)
print(tot)
