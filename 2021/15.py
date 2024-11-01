import sys
from collections import deque

cave = open("input/15", "r").read().splitlines()

mr, mc = len(cave), len(cave[0])


def find_neighbors(cur):
    (r, c) = cur
    neighbors = []
    dirs = {(0, 1), (1, 0), (-1, 0), (0, -1)}
    for d in dirs:
        if r + d[0] >= 0 and r + d[0] < mr and c + d[1] >= 0 and c + d[1] < mc:
            neighbors.append((r + d[0], c + d[1]))

    return neighbors


def get_path(target, prev):
    total_path = deque()
    u = target
    while u:
        total_path.appendleft(u)
        u = prev[u]
    return total_path


def find_value_of_lowest_risk_path(target):
    distance_from_start = {(i, j): sys.maxsize for j in range(mc) for i in range(mr)}
    prev = {(i, j): None for j in range(mc) for i in range(mr)}
    distance_from_start[(0, 0)] = 0
    q = deque(distance_from_start.keys())
    while q:
        cur = min(q, key=lambda x: distance_from_start[x])
        if cur == target:
            break
        q.remove(cur)

        neighbors = find_neighbors(cur)
        for neighbor in neighbors:
            if neighbor in q:
                potential_distance = distance_from_start[cur] + int(
                    cave[neighbor[0]][neighbor[1]]
                )
                if potential_distance < distance_from_start[neighbor]:
                    distance_from_start[neighbor] = potential_distance
                    prev[neighbor] = cur

    return sum(
        int(cave[x][y]) for (x, y) in get_path(target, prev) if not (x == 0 and y == 0)
    )


def part1():
    target = (mr - 1, mc - 1)
    print(find_value_of_lowest_risk_path(target))


if __name__ == "__main__":
    part1()
