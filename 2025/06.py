worksheet = open("input/6").read().splitlines()

def evaluate(nums, op):
    match op:
        case "+":
            return sum(nums)
        case "*":
            product = 1
            for num in nums:
                product *= num
            return product

def part1():
    numbers = [list(map(int, line.split())) for line in worksheet[:-1]]
    operators = worksheet[-1].split()

    total = 0
    for c in range(len(numbers[0])):
        op = operators[c]
        nums = [numbers[r][c] for r in range(len(numbers))]
        answer = evaluate(nums, op)
        total += answer
    return total

def part2():
    groups = []
    group = []

    cols = list(zip(*worksheet))
    for col in cols:
        if set(col) == {" "}:
            groups.append(group)
            group = []
        else:
            group.append(col)
    
    groups.append(group)

    total = 0
    for group in groups:
        op = group[0][-1]
        nums = []
        for t in group:
            num = []
            for el in t:
                if el != ' ' and el not in ("*", "+"):
                    num.append(el)
            nums.append(int("".join(num)))
            
        answer = evaluate(nums, op)
        total += answer
    return total


def main():
    print("Part 1:", part1())
    print("Part 2:", part2())

if __name__ == "__main__":
    main()
