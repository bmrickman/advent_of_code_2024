import re
import numpy as np

# note that in input.txt, all of the vectors are positive on both axis.
with open("./day13/input.txt", "r") as f:
    data = f.read().splitlines()
    vec_map = []
    for i in range(0, len(data), 4):
        aline = data[i]
        a_x = int(re.search("X+(.*),", aline).group(1)[1:])
        a_y = int(re.search("Y+(.*)", aline).group(1)[1:])
        bline = data[i + 1]
        b_x = int(re.search("X+(.*),", bline).group(1)[1:])
        b_y = int(re.search("Y+(.*)", bline).group(1)[1:])
        gline = data[i + 2]
        g_x = int(re.search("X=(.*),", gline).group(1))
        g_y = int(re.search("Y=(.*)", gline).group(1))
        vec_map.append((a_x, a_y, b_x, b_y, g_x, g_y))

tot = 0
for a_x, a_y, b_x, b_y, g_x, g_y in vec_map:
    if (
        a_x / b_x == a_y / b_y
    ):  # a and b are scalar multiples of each other, so just choose whichever has the better value prop
        if (
            a_x / b_x > 3
        ):  # a is more than 3 times the value of b, but costs exactly 3 times as muuch.  Use A.
            a_cnt = g_x / a_x
            tot += a_cnt * 3
        else:
            b_cnt = g_x / b_x
            tot += b_cnt
    else:
        A = np.array(((a_x, b_x), (a_y, b_y)))
        b = np.array((g_x, g_y))
        a_cnt, b_cnt = np.linalg.solve(A, b)
        a_cnt = np.around(a_cnt, decimals=5)
        b_cnt = np.around(b_cnt, decimals=5)
        if float.is_integer(a_cnt) and float.is_integer(b_cnt):
            tot += a_cnt * 3 + b_cnt
        else:
            pass

print(tot)
