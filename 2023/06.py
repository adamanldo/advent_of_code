races = open("input/6", "r").read().split("\n")

time = [int(x) for x in races[0].split()[1:]]
records = [int(x) for x in races[1].split()[1:]]


def part1():
    total = 1
    for race in range(len(time)):
        ways = 0
        for i in range(time[race]):
            if i * (time[race] - i) > records[race]:
                ways += 1
        total *= ways

    return total


def part2():
    ttime = int("".join(str(i) for i in time))
    record = int("".join(str(i) for i in records))

    ways = 0
    for i in range(ttime):
        if i * (ttime - i) > record:
            ways += 1

    return ways


# print(part1())
print(part2())
