data = open('input/7', 'r').read().split(',')
data = [int(i) for i in data]

def part1(data):
    minimum = 10000000
    for potential_solution in data:
        fuel = 0
        for num in data:
            fuel += abs(num - potential_solution)
        if fuel < minimum:
            minimum = fuel
    print(minimum)


def part2(data):
    minimum = 10000000000000000000
    d = {}
    for num in range(0, max(data) + 1):
        d[num] = sum((i for i in range(0, num + 1)))
    for potential_solution in range(0, max(data) + 1):
        fuel = 0
        for num in data:
            fuel += d[abs(potential_solution - num)]
        if fuel < minimum:
            minimum = fuel
    print(minimum)

part2(data)