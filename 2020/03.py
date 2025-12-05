grid = open("input/3").read().splitlines()
mr, mc = len(grid), len(grid[0])


def part1():
    x, y = 1, 3
    cr, cc = 0, 0
    trees = 0
    while cr < mr:
        if grid[cr][cc] == "#":
            trees += 1
        cr = cr + x
        cc = (cc + y) % mc

    return trees


def part2():
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    trees = 1
    for slope in slopes:
        x, y = slope[0], slope[1]
        cr, cc = 0, 0
        ctrees = 0
        while cr < mr:
            if grid[cr][cc] == "#":
                ctrees += 1
            cr = cr + x
            cc = (cc + y) % mc

        trees *= ctrees

    return trees


if __name__ == "__main__":
    print(part1())
    print(part2())
