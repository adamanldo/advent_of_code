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


part1()
