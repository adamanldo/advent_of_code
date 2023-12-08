num_range = open("input/4", "r").read()
start, end = map(int, num_range.split("-"))


def part1():
    total = 0

    for num in range(start, end):
        adjacent = False
        decreases = False
        prev_num = None
        for digit in list(str(num)):
            i = int(digit)
            if i == prev_num:
                adjacent = True
            if prev_num is not None:
                if i < prev_num:
                    decreases = True
            prev_num = i

        if adjacent and not decreases:
            total += 1

    return total


if __name__ == "__main__":
    print(part1())
