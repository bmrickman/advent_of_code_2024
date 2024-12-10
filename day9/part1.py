with open("./day9/input.txt", "r") as f:
    disk = f.read()
    disk = [int(char) for char in disk]

# WARNING:
# This implementation kind of sucks.
# see part 2 for a much cleaner version
l = 0
r = len(disk) - 1
i = 0
preallocate = sum(int(char) for char in disk)
i = 0
new_disk = []
rflag = True
rcacheval = None
rcachesize = 0
lturn = True
while l <= r:
    if (
        l == r and l % 2 == 0
    ):  # once they are matched, only the value at l/r hasn't been moved to new_disk
        if (
            rcachesize != 0
        ):  # if the cache for r exists, we've already moved some of the r values.
            val = l // 2
            count = disk[l]
            new_disk.extend([val] * rcachesize)
        else:
            val = l // 2
            count = disk[l]
            new_disk.extend([val] * count)
        break
    elif l == r:
        break
    elif lturn and l % 2 == 0:  # left and even
        val = l // 2
        count = disk[l]
        new_disk.extend([val] * count)
        l += 1
    elif lturn:  # left and odd
        lturn = False
        spots_to_fill = disk[l]
        l += 1
    elif not lturn:
        # initialize the cache if this is a new r index
        if rcachesize == 0:
            rcacheval = r // 2
            rcachesize = disk[r]
        # if the cache is too small to fill the gap, use what you can, then move on to the next iteration of r values
        if rcachesize <= spots_to_fill:
            new_disk.extend([rcacheval] * rcachesize)
            spots_to_fill = spots_to_fill - rcachesize
            rcachesize = 0  # we've used up the cache
            r = r - 2
        # if the cache has enough to fill the values
        elif rcachesize > spots_to_fill:  # cache stays initialized
            new_disk.extend([rcacheval] * spots_to_fill)
            rcachesize = rcachesize - spots_to_fill
            spots_to_fill = 0  # we've spilled all the spots
            lturn = True

print(sum(i * val for i, val in enumerate(new_disk)))
