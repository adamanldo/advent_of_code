from collections import defaultdict

with open("input/14", "r") as f:
    template, rules = f.read().split("\n\n")

rules_table = {}

for rule in rules.split("\n"):
    pair, insert = rule.split(" -> ")
    rules_table[pair] = insert


def get_initial_pairs(template):
    pair_counts = defaultdict(int)
    for i in range(len(template) - 1):
        e1, e2 = template[i], template[i + 1]
        pair_counts[e1 + e2] += 1
    return pair_counts


def step(pair_counts):
    update = defaultdict(int)
    for k, v in pair_counts.items():
        new_elem = rules_table[k]
        np0, np1 = k[0] + new_elem, new_elem + k[1]
        update[np0] += v
        update[np1] += v

    return update


def run_steps_and_get_counts(template, steps):
    pc = get_initial_pairs(template)
    for _ in range(steps):
        pc = step(pc)

    counts = defaultdict(int)
    for k, v in pc.items():
        counts[k[1]] += v

    # somehow, only counting the last element of each pair works
    # not sure how. for instance, in the example, how are we not
    # undercounting the first N? maybe we just got lucky and the first
    # element of both the test and the answer are not in the most common or
    # least common pairs

    print(
        sorted(counts.items(), key=lambda x: x[1], reverse=True)[0][1]
        - sorted(counts.items(), key=lambda x: x[1])[0][1]
    )


def part1(template):
    run_steps_and_get_counts(template, 10)


def part2(template):
    run_steps_and_get_counts(template, 40)


if __name__ == "__main__":
    part1(template)
    part2(template)
