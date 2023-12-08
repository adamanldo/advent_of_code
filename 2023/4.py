from collections import defaultdict


table = open("input/4", "r").read().split("\n")


def part1():
    total = 0
    for row in table:
        numbers = row.split(":")[1].strip().split(" | ")
        winning = set([int(i) for i in numbers[0].split()])
        mine = [int(i) for i in numbers[1].split()]
        first = True
        score = 0
        for num in mine:
            if num in winning:
                if first == True:
                    score = 1
                    first = False
                else:
                    score *= 2
        total += score

    return total


def part2():
    num_copies = defaultdict(lambda: 0)

    # originals
    for idx, row in enumerate(table):
        num_copies[idx] += 1

        numbers = row.split(":")[1].strip().split(" | ")
        winning = set([int(i) for i in numbers[0].split()])
        mine = [int(i) for i in numbers[1].split()]

        matches = 0
        for num in mine:
            if num in winning:
                matches += 1

        for i in range(matches):
            num_copies[idx + 1 + i] += num_copies[idx]

    return sum([v for _, v in num_copies.items()])


if __name__ == "__main__":
    # print(part1())
    print(part2())
