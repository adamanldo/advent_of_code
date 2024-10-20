mappings = [i for i in (open("input/6", "r").read().split("\n"))]


def part1():
    adj = {}
    for m in mappings:
        orbitee, orbiter = m.split(")")
        adj[orbiter] = orbitee

    direct, indirect = 0, 0
    for edge in adj:
        direct += 1
        cur = adj[edge]
        while cur != "COM":
            indirect += 1
            cur = adj[cur]

    print(direct + indirect)


def part2():
    adj = {}
    for m in mappings:
        orbitee, orbiter = m.split(")")
        adj[orbiter] = orbitee

    source = adj["YOU"]
    target = adj["SAN"]

    cur = source
    path_from_source_to_root = set()
    while cur != "COM":
        path_from_source_to_root.add(cur)
        cur = adj[cur]

    cur = target
    closest_shared_parent = None
    while cur != "COM":
        if cur in path_from_source_to_root:
            closest_shared_parent = cur
            break
        cur = adj[cur]

    cur = source
    distance_from_source_to_shared_parent = 0
    while cur != closest_shared_parent:
        distance_from_source_to_shared_parent += 1
        cur = adj[cur]

    cur = target
    distance_from_target_to_shared_parent = 0
    while cur != closest_shared_parent:
        distance_from_target_to_shared_parent += 1
        cur = adj[cur]

    print(distance_from_source_to_shared_parent + distance_from_target_to_shared_parent)


if __name__ == "__main__":
    # part1()
    part2()
