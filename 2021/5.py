from collections import Counter
with open('input/5', 'r') as f:
    segments = [line.replace(' -> ', ',') for line in f.read().split('\n')]

def part1():
    lines = []
    for line in segments:
        x1, y1, x2, y2 = map(int, line.split(','))
        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    lines.append((x, y))

    position_count = Counter(lines)
    print(len([k for k,v in position_count.items() if v > 1]))

part1()

def part2():
    lines = []
    for line in segments:
        x1, y1, x2, y2 = map(int, line.split(','))
        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    lines.append((x, y))
        elif y2 > y1:
            if x2 > x1:
                for idx, x in enumerate(range(min(x1, x2), max(x1, x2) + 1)):
                    lines.append((x, y1 + idx))
            else:
                for idx, x in enumerate(range(max(x1, x2), min(x1, x2) - 1, -1)):
                    lines.append((x, y1 + idx))
        else:
            if x2 > x1:
                for idx, x in enumerate(range(min(x1, x2), max(x1, x2) + 1)):
                    lines.append((x, y1 - idx))
            else:
                for idx, x in enumerate(range(max(x1, x2), min(x1, x2) - 1, -1)):
                    lines.append((x, y1 - idx))


    position_count = Counter(lines)
    print(len([k for k,v in position_count.items() if v > 1]))

part2()