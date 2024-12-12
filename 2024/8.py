from collections import defaultdict

scan = list(map(list, open("input/8").read().splitlines()))
mr, mc = len(scan), len(scan[0])

antennas = defaultdict(list)
for i in range(mr):
    for j in range(mc):
        if scan[i][j] != ".":
            antennas[scan[i][j]].append((i, j))


def part1():
    antinodes = set()
    for antenna in antennas.values():
        for idx, point in enumerate(antenna):
            for other_point in antenna[idx + 1 :]:
                x1, y1 = point[0], point[1]
                x2, y2 = other_point[0], other_point[1]
                a1 = (
                    x1 + x1 - x2,
                    y1 + y1 - y2,
                )
                a2 = (
                    x2 + x2 - x1,
                    y2 + y2 - y1,
                )
                if 0 <= a1[0] < mr and 0 <= a1[1] < mc:
                    antinodes.add(a1)
                if 0 <= a2[0] < mr and 0 <= a2[1] < mc:
                    antinodes.add(a2)
    return len(antinodes)


def part2():
    antinodes = set()
    for antenna in antennas.values():
        for idx, point in enumerate(antenna):
            for other_point in antenna[idx + 1 :]:
                x1, y1 = point[0], point[1]
                x2, y2 = other_point[0], other_point[1]
                x, y = x1, y1
                while True:
                    x = x + x1 - x2
                    y = y + y1 - y2

                    if 0 <= x < mr and 0 <= y < mc:
                        antinodes.add((x, y))
                    else:
                        break
                x, y = x2, y2
                while True:
                    x = x + x1 - x2
                    y = y + y1 - y2

                    if 0 <= x < mr and 0 <= y < mc:
                        antinodes.add((x, y))
                    else:
                        break
                x, y = x2, y2
                while True:
                    x = x + x2 - x1
                    y = y + y2 - y1

                    if 0 <= x < mr and 0 <= y < mc:
                        antinodes.add((x, y))
                    else:
                        break
                x, y = x1, y1
                while True:
                    x = x + x2 - x1
                    y = y + y2 - y1

                    if 0 <= x < mr and 0 <= y < mc:
                        antinodes.add((x, y))
                    else:
                        break
    return len(antinodes)


if __name__ == "__main__":
    print(part1())
    print(part2())
