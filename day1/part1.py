with open("./day1/input.txt", "r") as f:
    data = f.read().splitlines()

left_nums = []
right_nums = []
for line in data:
    l, r = line.split()
    left_nums.append(l)
    right_nums.append(r)

left_nums = sorted(left_nums)
right_nums = sorted(right_nums)

data = zip(left_nums, right_nums)
total_dist = 0
for l, r in data:
    total_dist += abs(int(l) - int(r))

print(total_dist)
