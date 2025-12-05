data = open("input/3").read().splitlines()
banks = [list(map(int, line)) for line in data]

def part1():
    total = 0
    for bank in banks:
        m = 0
        for i in range(len(bank)):
            for j in range(i+1, len(bank)):
                potential_max = bank[i] * 10 + bank[j]
                if potential_max > m:
                    m = potential_max
        total += m

    return total 

def part2():
    total = 0
    for bank in banks:
        jolts = 0
        for idx in range(11):
            digit = max(bank[:idx - 11])
            bank = bank[bank.index(digit) + 1:]
            jolts = (jolts * 10) + digit
        jolts = (jolts * 10) + max(bank)
        total += jolts

    return total 

if __name__ == "__main__":
    print(part1())
    print(part2())