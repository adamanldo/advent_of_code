import functools

with open('input/9', 'r') as f:
    heightmap = f.read().split('\n')

ROW_MAX = len(heightmap)
COL_MAX = len(heightmap[0])

def is_low_point(row_idx, col_idx) -> bool:
    adjacent_indexes = []
    if row_idx > 0:
        adjacent_indexes.append((row_idx - 1, col_idx))
    if row_idx + 1 < ROW_MAX:
        adjacent_indexes.append((row_idx + 1, col_idx))
    if col_idx > 0:
        adjacent_indexes.append((row_idx, col_idx - 1))
    if col_idx + 1 < COL_MAX:
        adjacent_indexes.append((row_idx, col_idx + 1))
    return (all(int(heightmap[row_idx][col_idx]) < int(heightmap[row][col]) for row, col in adjacent_indexes))

def part_1():
    res = 0
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            if is_low_point(i, j):
                res += int(heightmap[i][j]) + 1

    print(res)

def find_adjacent_edges(row_idx, col_idx):
    adjacent_indexes = []
    if row_idx > 0:
        if heightmap[row_idx - 1][col_idx] != '9':
            adjacent_indexes.append((row_idx - 1, col_idx))
    if row_idx + 1 < ROW_MAX:
        if heightmap[row_idx + 1][col_idx] != '9':
            adjacent_indexes.append((row_idx + 1, col_idx))
    if col_idx > 0:
        if heightmap[row_idx][col_idx - 1] != '9':
            adjacent_indexes.append((row_idx, col_idx - 1))
    if col_idx + 1 < COL_MAX:
        if heightmap[row_idx][col_idx + 1] != '9':
            adjacent_indexes.append((row_idx, col_idx + 1))
    return adjacent_indexes

def dfs(visited, row_idx, col_idx):
    if (row_idx, col_idx) not in visited:
        visited.add((row_idx, col_idx))
        for node in find_adjacent_edges(row_idx, col_idx):
            dfs(visited, node[0], node[1])

def part2():
    basins = []
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            if is_low_point(i, j):
                visited = set()
                dfs(visited, i, j)
                basins.append(visited)
    print(functools.reduce(lambda a,b: a*b, [len(basin) for basin in sorted(basins, key=len, reverse=True)[0:3]]))

part2()