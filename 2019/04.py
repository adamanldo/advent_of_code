num_range = open("input/4", "r").read()
start, end = map(int, num_range.split("-"))


def has_any_pair_of_adjacent_digits(num):
    cur, count = None, 0
    for digit in list(str(num)):
        if digit == cur:
            count += 1
        else:
            cur, count = digit, 1
        if count >= 2:
            return True


def has_standalone_pair_of_adjacent_digits(num):
    cur, count = None, 0
    for digit in list(str(num)):
        if digit == cur:
            count += 1
        else:
            if count == 2:
                return True
            cur, count = digit, 1
    if count == 2:
        return True


def never_decreases(num):
    digits = list(str(num))
    for i in range(1, len(digits)):
        if int(digits[i]) < int(digits[i - 1]):
            return False
    return True


def part1():
    total = 0

    for num in range(start, end):
        if has_any_pair_of_adjacent_digits(num) and never_decreases(num):
            total += 1

    print(total)


def part2():
    total = 0

    for num in range(start, end):
        if has_standalone_pair_of_adjacent_digits(num) and never_decreases(num):
            total += 1

    print(total)


if __name__ == "__main__":
    part1()
    part2()
