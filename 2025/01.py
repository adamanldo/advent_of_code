data = open("input/1").read().splitlines()
rotations = [(r[0], int(r[1:]))  for r in data]

def part1():
    dial_pos = 50
    total_zeroes = 0
    for r in rotations:
        direction, distance = r
        if direction == "L":
            dial_pos = (dial_pos - distance) % 100
        elif direction == "R":
            dial_pos = (dial_pos + distance) % 100
        if dial_pos == 0:
            total_zeroes += 1
        
    return total_zeroes

def part2():
    dial_pos = 50
    total_zeroes = 0
    for r in rotations:
        direction, distance = r
        if direction == "L":
            step = -1
        elif direction == "R":
            step = 1
        
        for _ in range(distance):
            dial_pos = (dial_pos + step) % 100
            if dial_pos == 0:
                total_zeroes += 1
        
    return total_zeroes

if __name__ == "__main__":
    print(part1())
    print(part2())