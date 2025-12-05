data = open("input/1", "r").read().split("\n")


def part1():
    total = 0
    for line in data:
        l = list(line)
        n = []
        for i in l:
            if i.isdigit():
                n.append(i)

        total += int(n[0] + n[-1])

    return total


def part2():
    total = 0
    valid_str_nums = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    subbed = []
    for line in data:
        l = []
        cur = list(line)
        for i in range(len(line)):
            if line[i].isdigit():
                l.append(int(line[i]))
                continue

            for v in valid_str_nums:
                if list(v) == cur[i : i + len(v)]:
                    l.append(valid_str_nums[v])
        subbed.append(l)

    total = 0
    for line in subbed:
        total += int(str(line[0]) + str(line[-1]))

    return total


if __name__ == "__main__":
    # print(part1())
    print(part2())
