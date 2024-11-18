from collections import Counter
data = open('input/2').read().splitlines()

def part1():
    valid = 0
    for line in data:
        must_appear, char, password = line.split(" ")
        must_appear = tuple(map(int, must_appear.split("-")))
        char = char[0]

        c = Counter(password)
        if must_appear[0] <= c[char] <= must_appear[1]:
            valid += 1

    return valid 

def part2():
    valid = 0
    for line in data:
        must_appear, char, password = line.split(" ")
        must_appear = tuple(map(int, must_appear.split("-")))
        char = char[0]

        if ((password[must_appear[0] - 1] == char) is not (password[must_appear[1] - 1] == char)):
            valid += 1
    
    return valid

if __name__ == "__main__":
    print(part1())
    print(part2())