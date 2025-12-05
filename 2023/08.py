import re
from itertools import cycle
from math import lcm

lr, nodes = open("input/8", "r").read().split("\n\n")


def part1():
    network = {}
    for row in nodes.split("\n"):
        node, rest = row.split(" = ")
        possible_path = re.findall(r"\w+", rest)

        network[node] = tuple(possible_path)

    dirs = cycle(lr)
    steps = 0
    cur = "AAA"
    while cur != "ZZZ":
        cur_dir = next(dirs)
        if cur_dir == "L":
            cur = network[cur][0]
        elif cur_dir == "R":
            cur = network[cur][1]
        steps += 1

    return steps


def part2():
    network = {}
    for row in nodes.split("\n"):
        node, rest = row.split(" = ")
        possible_path = re.findall(r"\w+", rest)

        network[node] = tuple(possible_path)

    start_nodes = []
    for node in network.keys():
        if node.endswith("A"):
            start_nodes.append(node)

    cycle_lengths = []
    for node in start_nodes:
        dirs = cycle(lr)
        steps = 0
        cur_node = node
        while not (cur_node.endswith("Z")):
            cur_dir = next(dirs)
            if cur_dir == "L":
                cur_node = network[cur_node][0]
            elif cur_dir == "R":
                cur_node = network[cur_node][1]
            steps += 1
        cycle_lengths.append(steps)

    return lcm(*cycle_lengths)


if __name__ == "__main__":
    # print(part1())
    print(part2())
