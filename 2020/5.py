from math import ceil

seats = open("input/5").read().splitlines()


def part1():
    seat_ids = []
    for seat in seats:
        l, r = 0, 127
        for rd in seat[0:8]:
            if rd == "F":
                r = r - ceil((r - l) / 2)
            elif rd == "B":
                l = l + ceil((r - l) / 2)
        row = l
        l, r = 0, 7
        for cd in seat[7:11]:
            if cd == "R":
                l = l + ceil((r - l) / 2)
            elif cd == "L":
                r = r - ceil((r - l) / 2)
        col = l

        seat_ids.append((row * 8) + col)

    return sorted(seat_ids, reverse=True)[0]


def part2():
    seat_ids = []
    seats_map = []
    for seat in seats:
        l, r = 0, 127
        for rd in seat[0:8]:
            if rd == "F":
                r = r - ceil((r - l) / 2)
            elif rd == "B":
                l = l + ceil((r - l) / 2)
        row = l
        l, r = 0, 7
        for cd in seat[7:11]:
            if cd == "R":
                l = l + ceil((r - l) / 2)
            elif cd == "L":
                r = r - ceil((r - l) / 2)
        col = l

        seats_map.append((row, col))
        seat_ids.append((row * 8) + col)

    for i in range(128):
        for j in range(8):
            if (i, j) not in seats_map and (
                (((i * 8) + j) + 1) in seat_ids and (((i * 8) + j) - 1) in seat_ids
            ):
                return (i * 8) + j


if __name__ == "__main__":
    print(part1())
    print(part2())
