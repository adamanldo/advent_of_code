data = list(map(int, open('input/1').read().splitlines()))

def part1():
    for idx, num in enumerate(data):
        diff = 2020 - num
        for potential_entry in data[idx:]:
            if potential_entry == diff:
                return potential_entry * num

def part2():
    for idx, num in enumerate(data):
        diff = 2020 - num
        for idx2, potential_entry in enumerate(data[idx:]):
            diff2 = diff - potential_entry
            for potential_entry2 in data[idx2:]:
                if potential_entry2 == diff2:
                    return num * potential_entry * potential_entry2


if __name__ == "__main__":
    print(part1())
    print(part2())