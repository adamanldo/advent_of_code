data = [int(i) for i in (open("input/1", "r").read().split("\n"))]


def part1():
    total = 0
    for mass in data:
        fuel_required = mass // 3 - 2
        total += fuel_required

    print(total)


def part2():
    total = 0
    for mass in data:
        total += extra_fuel_required(mass)

    print(total)


def extra_fuel_required(mass):
    res = mass // 3 - 2
    if res <= 0:
        return 0
    else:
        return res + extra_fuel_required(res)


if __name__ == "__main__":
    # part1()
    part2()
