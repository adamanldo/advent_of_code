from collections import defaultdict

rules = open("input/7").read().splitlines()


def part1():
    bag_map = parse_rules(rules)
    return get_outermost_bag_contains("shiny gold", bag_map)


def part2():
    bag_map = parse_rules2(rules)
    return get_individual_bags((1, "shiny gold"), bag_map)


def get_individual_bags(bag, bag_map):
    _, color = bag
    total = 0
    for b in bag_map[color]:
        total += b[0] * (1 + get_individual_bags(b, bag_map))

    return total


def get_outermost_bag_contains(bag, bag_map, visited=set()):
    for new_bag in bag_map[bag]:
        if new_bag not in visited:
            visited.add(new_bag)
            get_outermost_bag_contains(new_bag, bag_map, visited)

    return len(visited)


def parse_rules(rules):
    bag_map = defaultdict(list)
    for rule in rules:
        outer_bag, inner_bags = rule.split(" contain ")
        outer_bag = outer_bag.split(" bags")[0]

        inner_bags = inner_bags.strip(".").split(", ")
        for i, bag in enumerate(inner_bags):
            if bag[-4:] == " bag":
                inner_bags[i] = bag[2:][:-4]
            else:
                if bag != "no other bags":
                    inner_bags[i] = bag[2:][:-5]

        for i_bag in inner_bags:
            bag_map[i_bag].append(outer_bag)

    return bag_map


def parse_rules2(rules):
    bag_map = defaultdict(list)
    for rule in rules:
        outer_bag, inner_bags = rule.split(" contain ")
        inner_bags = inner_bags.strip(".").split(", ")
        for i, bag in enumerate(inner_bags):
            if bag[-4:] == " bag":
                inner_bags[i] = (int(bag[:2]), bag[2:][:-4])
            else:
                if bag != "no other bags":
                    inner_bags[i] = (int(bag[:2]), bag[2:][:-5])
        outer_bag = outer_bag.split(" bags")[0]

        for i_bag in inner_bags:
            if i_bag != "no other bags":
                bag_map[outer_bag].append(i_bag)

    return bag_map


if __name__ == "__main__":
    print(part1())
    print(part2())
