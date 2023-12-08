data = open("input/3", "r").read().split("\n")


def part1():
    positions_to_part, num_groups = find_groups(data)

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    res = []
    for line_idx, line in enumerate(data):
        for char_idx, char in enumerate(line):
            if not char.isdigit() and char != ".":
                for d in dirs:
                    pos = (line_idx + d[0], char_idx + d[1])
                    if pos in positions_to_part:
                        num = positions_to_part[pos]
                        same_number = num_groups[pos]
                        res.append(num)

                        # clear values from the same number group
                        positions_to_part = {
                            k: v
                            for k, v in positions_to_part.items()
                            if k not in same_number
                        }
    return sum([int(i) for i in res])


def part2():
    positions_to_part, num_groups = find_groups(data)

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    gear_ratios = []
    for line_idx, line in enumerate(data):
        for char_idx, char in enumerate(line):
            if char == "*":
                adjacent_part_nums = 0
                gears = []
                for d in dirs:
                    pos = (line_idx + d[0], char_idx + d[1])
                    if pos in positions_to_part:
                        adjacent_part_nums += 1
                        num = positions_to_part[pos]
                        same_number = num_groups[pos]
                        gears.append(num)

                        # clear values from the same number group
                        positions_to_part = {
                            k: v
                            for k, v in positions_to_part.items()
                            if k not in same_number
                        }

                if adjacent_part_nums == 2:
                    gear_ratio = int(gears[0]) * int(gears[1])
                    gear_ratios.append(gear_ratio)

    return sum(gear_ratios)


def find_groups(data):
    positions_to_part = {}
    num_groups = {}
    for line_idx, line in enumerate(data):
        num = ""
        number_positions = []
        for char_idx, char in enumerate(line):
            if char.isdigit():
                num += char
                number_positions.append((line_idx, char_idx))

            # we've reached the end of a number, save state
            else:
                if num and number_positions:
                    for pos in number_positions:
                        positions_to_part[pos] = num
                    for i in number_positions:
                        groups = []
                        for j in number_positions:
                            groups.append(j)
                        num_groups[i] = groups

                    # clear state
                    num = ""
                    number_positions = []

        # end of line
        if num and number_positions:
            for pos in number_positions:
                positions_to_part[pos] = num
            for i in number_positions:
                groups = []
                for j in number_positions:
                    groups.append(j)
                num_groups[i] = groups

            # clear state
            num = ""
            number_positions = []

    return positions_to_part, num_groups


if __name__ == "__main__":
    # print(part1())
    print(part2())
