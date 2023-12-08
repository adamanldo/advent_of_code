almanac = open("input/5", "r").read().split("\n\n")


def part1():
    seeds = [int(i) for i in almanac[0].split(":")[1].split()]

    locations = []
    for seed in seeds:
        locations.append(get_location(seed))

    return min(locations)


def part2():
    seeds = [int(i) for i in almanac[0].split(":")[1].split()]
    seed_ranges = [seeds[i : i + 2] for i in range(0, len(seeds), 2)]

    locations = []
    for seed in seeds:
        locations.append(get_location(seed))


def get_location(seed):
    current_val = [seed]
    for mp in almanac[1:]:
        cur = current_val.pop()
        map_res = None
        for line in mp.split("\n")[1:]:
            dest_start, source_start, length = [int(i) for i in line.split()]
            if cur >= source_start and cur < source_start + length:
                offset = dest_start - source_start
                map_res = cur + offset
        if not map_res:
            map_res = cur
        current_val.append(map_res)

    return current_val.pop()


def get_seed(location):
    current_val = [location]
    for mp in almanac[1:][::-1]:
        cur = current_val.pop()
        map_res = None
        for line in mp.split("\n")[1:]:
            source_start, dest_start, length = [int(i) for i in line.split()]
            if cur >= source_start and cur < source_start + length:
                offset = dest_start - source_start
                map_res = cur + offset
        if not map_res:
            map_res = cur
        current_val.append(map_res)

    return current_val.pop()


# print(part1())
print(part2())
