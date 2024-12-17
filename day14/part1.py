from collections import defaultdict

with open("./day14/input.txt", "r") as f:
    _data = f.read().splitlines()
    data = []
    for line in _data:
        p, v = line[2:].split()
        p_x, p_y = p.split(",")
        v_x, v_y = v[2:].split(",")
        data.append((int(x) for x in (p_x, p_y, v_x, v_y)))

quadrants = defaultdict(lambda: 0)
for p_x, p_y, v_x, v_y in data:  # iterate over robots
    # calcualte location from velocity
    p_x = p_x + v_x * 100
    p_y = p_y + v_y * 100
    # calculate position after wraps (this works for negatives too!)
    p_x = p_x % 101
    p_y = p_y % 103
    # calculate quadrant
    if p_x == 50 or p_y == 51:
        pass
    elif p_x > 50 and p_y > 51:
        quadrants["br"] += 1
    elif p_x > 50 and p_y < 51:
        quadrants["tr"] += 1
    elif p_x < 50 and p_y > 51:
        quadrants["bl"] += 1
    elif p_x < 50 and p_y < 51:
        quadrants["tl"] += 1


print(quadrants.values())
