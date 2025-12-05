reports = open("input/2").read().splitlines()


def part1():
    num_safe = 0
    for report in reports:
        levels = [int(x) for x in report.split()]
        all_decreasing, all_increasing = True, True
        within_distance = True
        for i in range(1, len(levels)):
            if levels[i] < levels[i - 1]:
                all_increasing = False
            if levels[i] > levels[i - 1]:
                all_decreasing = False
            if not 1 <= abs((levels[i] - levels[i - 1])) <= 3:
                within_distance = False
        if (all_increasing or all_decreasing) and within_distance:
            num_safe += 1

    return num_safe


def part2():
    num_safe = 0
    for report in reports:
        levels = [int(x) for x in report.split()]
        all_decreasing, all_increasing = True, True
        within_distance = True
        for i in range(1, len(levels)):
            if levels[i] < levels[i - 1]:
                all_increasing = False
            if levels[i] > levels[i - 1]:
                all_decreasing = False
            if not 1 <= abs((levels[i] - levels[i - 1])) <= 3:
                within_distance = False
        if (all_increasing or all_decreasing) and within_distance:
            num_safe += 1
        elif any(is_safe_without(levels, i) for i in range(len(levels))):
            num_safe += 1

    return num_safe


def is_safe_without(levels, idx):
    levels = levels[:idx] + levels[idx + 1 :]
    all_decreasing, all_increasing = True, True
    within_distance = True
    for i in range(1, len(levels)):
        if levels[i] < levels[i - 1]:
            all_increasing = False
        if levels[i] > levels[i - 1]:
            all_decreasing = False
        if not 1 <= abs((levels[i] - levels[i - 1])) <= 3:
            within_distance = False
    if (all_increasing or all_decreasing) and within_distance:
        return True
    else:
        return False


if __name__ == "__main__":
    print(part1())
    print(part2())
