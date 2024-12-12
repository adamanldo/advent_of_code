import itertools

equations = open("input/7").read().splitlines()


def part1():
    calibration_result = 0
    for line in equations:
        test_value, nums = line.split(":")
        test_value = int(test_value)
        nums = list(map(int, nums.split()))
        ops = ["*", "+"]
        combos = list(itertools.product(ops, repeat=len(nums) - 1))
        for combo in combos:
            n1, n2 = 0, 1
            prev = nums[n1]
            for op in combo:
                solution = eval(str(prev) + op + str(nums[n2]))
                prev = solution
                n2 += 1
            if solution == test_value:
                calibration_result += test_value
                break

    return calibration_result


def part2():
    calibration_result = 0
    for line in equations:
        test_value, nums = line.split(":")
        test_value = int(test_value)
        nums = list(map(int, nums.split()))
        ops = ["*", "+", ""]
        combos = list(itertools.product(ops, repeat=len(nums) - 1))
        for combo in combos:
            n1, n2 = 0, 1
            prev = nums[n1]
            for op in combo:
                solution = eval(str(prev) + op + str(nums[n2]))
                prev = solution
                n2 += 1
            if solution == test_value:
                calibration_result += test_value
                break

    return calibration_result


if __name__ == "__main__":
    print(part1())
    print(part2())
