from collections import Counter
data = open("input/1").read().splitlines()

def part1():
    left, right = [], []
    for line in data:
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)

    left.sort()
    right.sort()

    res = 0
    for i in range(len(data)):
        diff = abs(left[i] - right[i])
        res += diff
    
    return res

def part2():
    left, right = [], []
    for line in data:
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)

    left.sort()
    right.sort()

    rc = Counter(right)
    res = 0
    for i in range(len(data)):
        res += left[i] * rc[left[i]]
    return res

if __name__ == "__main__":
    print(part1())
    print(part2())