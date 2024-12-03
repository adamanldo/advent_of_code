import re

data = open("input/3").read()


def part1():
    valid_insts = re.findall("mul\((\d+,\d+)\)", data)
    res = 0
    for inst in valid_insts:
        x, y = map(int, inst.split(","))
        res += x * y

    return res


def part2():
    valid_insts = re.findall("mul\((\d+,\d+)\)|(do\(\))|(don't\(\))", data)
    valid_insts = [s for group in valid_insts for s in group if s]

    enabled = True
    res = 0
    for inst in valid_insts:
        if inst == "do()":
            enabled = True
            continue
        elif inst == "don't()":
            enabled = False
            continue
        if not enabled:
            continue
        x, y = map(int, inst.split(","))
        res += x * y
    return res


if __name__ == "__main__":
    print(part1())
    print(part2())
