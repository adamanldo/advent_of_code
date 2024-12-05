from collections import defaultdict
from functools import cmp_to_key

order_rules, updates = [x.splitlines() for x in open("input/5").read().split("\n\n")]


def part1():
    before = defaultdict(list)
    after = defaultdict(list)
    for rule in order_rules:
        a, b = map(int, rule.split("|"))
        before[b].append(a)
        after[a].append(b)

    middle_page_sum = 0
    for update in updates:
        page_nums = list(map(int, update.split(",")))

        ordered = True
        for idx, page in enumerate(page_nums):
            prev = page_nums[:idx]
            forward = page_nums[idx + 1 :]
            for p in prev:
                if page in before and idx > 0:
                    if p not in before[page]:
                        ordered = False

            for f in forward:
                if page in after and idx < len(page_nums):
                    if f not in after[page]:
                        ordered = False

        if ordered:
            middle = len(page_nums) // 2
            middle_page_sum += page_nums[middle]

    return middle_page_sum


def part2():
    def sort_pages(a, b):
        if b in before[a] and a in after[b]:
            return -1
        elif a in before[b] and b in after[a]:
            return 1

    before = defaultdict(list)
    after = defaultdict(list)
    for rule in order_rules:
        a, b = map(int, rule.split("|"))
        before[b].append(a)
        after[a].append(b)

    middle_page_sum = 0
    for update in updates:
        page_nums = list(map(int, update.split(",")))

        ordered = True
        for idx, page in enumerate(page_nums):
            prev = page_nums[:idx]
            forward = page_nums[idx + 1 :]
            for p in prev:
                if page in before and idx > 0:
                    if p not in before[page]:
                        ordered = False

            for f in forward:
                if page in after and idx < len(page_nums):
                    if f not in after[page]:
                        ordered = False

        if not ordered:
            s = sorted(page_nums, key=cmp_to_key(sort_pages))
            middle = len(page_nums) // 2
            middle_page_sum += s[middle]

    return middle_page_sum


if __name__ == "__main__":
    print(part1())
    print(part2())
