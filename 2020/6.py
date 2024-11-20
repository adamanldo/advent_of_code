from collections import Counter

group_answers = open("input/6").read().split("\n\n")


def part1():
    ans = 0
    for group in group_answers:
        c = Counter([char for line in group.splitlines() for char in line])
        ans += len(c)
    return ans


def part2():
    ans = 0
    for group in group_answers:
        individual_answers = group.splitlines()
        c = Counter([char for line in individual_answers for char in line])
        for answer in c:
            if c[answer] == len(individual_answers):
                ans += 1
    return ans


if __name__ == "__main__":
    print(part1())
    print(part2())
