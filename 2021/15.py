import heapq

data = open("input/15", "r").read().splitlines()
cave = list(list(map(int, row)) for row in data)


def find_neighbors(cur, mr, mc):
    (r, c) = cur
    neighbors = []
    dirs = {(0, 1), (1, 0), (-1, 0), (0, -1)}
    for d in dirs:
        if r + d[0] >= 0 and r + d[0] < mr and c + d[1] >= 0 and c + d[1] < mc:
            neighbors.append((r + d[0], c + d[1]))

    return neighbors


def find_value_of_lowest_risk_path(grid):
    mr, mc = len(grid), len(grid[0])
    target = (mr - 1, mc - 1)

    distance_from_start = {(i, j): float("inf") for j in range(mc) for i in range(mr)}
    distance_from_start[(0, 0)] = 0
    prev = {(i, j): None for j in range(mc) for i in range(mr)}

    q = [(0, (0, 0))]
    heapq.heapify(q)
    visited = set()

    while q:
        dist, node = heapq.heappop(q)
        if node == target:
            return dist

        if node in visited:
            continue

        visited.add(node)

        neighbors = find_neighbors(node, mr, mc)
        for neighbor in neighbors:
            nr, nc = neighbor
            potential_distance = distance_from_start[node] + int(grid[nr][nc])
            if potential_distance < distance_from_start[neighbor]:
                distance_from_start[neighbor] = potential_distance
                prev[neighbor] = node
                heapq.heappush(q, (potential_distance, neighbor))


def generate_full_cave_map(cave):
    mr, mc = len(cave), len(cave[0])
    for _ in range(4):
        for row in cave:
            tail = row[-mr:]
            row.extend((x + 1) if x < 9 else 1 for x in tail)

    for _ in range(4):
        for row in cave[-mc:]:
            row = [(x + 1) if x < 9 else 1 for x in row]
            cave.append(row)

    return cave


def part1():
    print("Part 1: " + str(find_value_of_lowest_risk_path(cave)))


def part2():
    full_cave = generate_full_cave_map(cave)
    print("Part 2: " + str(find_value_of_lowest_risk_path(full_cave)))


if __name__ == "__main__":
    part1()
    part2()
