from itertools import cycle


guard_map = list(map(list, open("input/6").read().splitlines()))

mr, mc = len(guard_map), len(guard_map[0])


def part1():
    # up, right, down, left
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    current_dir = dirs[0]
    dir_cycle = cycle(dirs)
    next(dir_cycle)
    for i in range(mr):
        for j in range(mc):
            if guard_map[i][j] == "^":
                gx, gy = i, j
                visited.add((gx, gy))
                break

    while 0 <= gx < mr and 0 <= gy < mc:
        gx, gy = (
            gx + current_dir[0],
            gy + current_dir[1],
        )
        if 0 <= gx < mr and 0 <= gy < mc:
            visited.add((gx, gy))

        # check the next position in this direction to see if we need to change direction
        ngx, ngy = gx + current_dir[0], gy + current_dir[1]
        if 0 <= ngx < mr and 0 <= ngy < mc:
            if guard_map[ngx][ngy] == "#":
                current_dir = next(dir_cycle)

    return len(visited)


def causes_loop(guard_start, guard_map):
    # play out the full path, if the guard ever hits a position
    # he's already been in while going the same direction, it is a loop

    # up, right, down, left
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    current_dir = dirs[0]
    dir_cycle = cycle(dirs)
    next(dir_cycle)
    gx, gy = guard_start

    while True:
        visited.add(((gx, gy), current_dir))
        if not (0 <= gx < mr and 0 <= gy < mc):
            return False

        # check the next position in this direction to see if we need to change direction
        ngx, ngy = gx + current_dir[0], gy + current_dir[1]
        if 0 <= ngx < mr and 0 <= ngy < mc:
            # if its an obstacle, we should switch direction and check if we've
            # already been in our current position with that direction
            # next iteration we will add it to the visited set
            if guard_map[ngx][ngy] == "#":
                current_dir = next(dir_cycle)
                if ((gx, gy), current_dir) in visited:
                    return True
            # otherwise, we can move in that direction
            else:
                gx, gy = ngx, ngy
        else:
            return False


def part2():
    for i in range(mr):
        for j in range(mc):
            if guard_map[i][j] == "^":
                guard_start = (i, j)
                break

    # check each position for potential obstacles
    res = 0
    for i in range(mr):
        for j in range(mc):
            if guard_map[i][j] == ".":
                guard_map[i][j] = "#"
                if causes_loop(guard_start, guard_map):
                    res += 1
                guard_map[i][j] = "."
    return res


if __name__ == "__main__":
    print(part1())
    print(part2())
