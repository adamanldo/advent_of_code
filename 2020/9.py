numbers = [int(x) for x in open("input/9").read().splitlines()]


def part1():
    preamble = 25
    for idx, num in enumerate(numbers):
        if idx < preamble:
            continue
        prev = numbers[idx - preamble : idx]
        if not any(num - p in prev for p in prev):
            return num


def part2():
    preamble = 25
    invalid_num = None
    for idx, num in enumerate(numbers):
        if idx < preamble:
            continue
        prev = numbers[idx - preamble : idx]
        if not any(num - p in prev for p in prev):
            invalid_num = num

    # can we just brute force?
    i, j = find_subarrays_sum_to_target(numbers, invalid_num)

    nums = numbers[i:j]
    return min(nums) + max(nums)


def find_subarrays_sum_to_target(arr, target):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if sum(numbers[i:j]) == target:
                return i, j


if __name__ == "__main__":
    print(part1())
    print(part2())
