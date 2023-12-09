histories = open("input/9", "r").read().split("\n")


def part1():
    total = 0
    for history in histories:
        history = [int(x) for x in history.split()]
        extrapolated = history[-1] + get_next_value(history)
        total += extrapolated
    return total


def part2():
    total = 0
    for history in histories:
        history = [int(x) for x in history.split()]
        extrapolated = history[0] - get_previous_value(history)
        total += extrapolated
    return total


def get_next_value(seq):
    if all(s == 0 for s in seq):
        return 0
    else:
        differences = []
        for i in range(1, len(seq)):
            differences.append(seq[i] - seq[i - 1])
        next_in_seq = get_next_value(differences)
        return differences[-1] + next_in_seq


def get_previous_value(seq):
    if all(s == 0 for s in seq):
        return 0
    else:
        differences = []
        for i in range(1, len(seq)):
            differences.append(seq[i] - seq[i - 1])
        prev_in_seq = get_previous_value(differences)
        return differences[0] - prev_in_seq


if __name__ == "__main__":
    # print(part1())
    print(part2())
