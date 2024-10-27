import sys

sys.setrecursionlimit(1000000)

grid = [list(l) for l in open("input/10", "r").read().split("\n")]
ROW_MAX = len(grid[0])
COL_MAX = len(grid)


def part1():
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                visited.add((i, j))
                dfs(i, j, START_DIRS, visited)
    return len(visited) // 2


PIPE_DIRS = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(0, -1), (-1, 0)],
    "7": [(0, -1), (1, 0)],
    "F": [(1, 0), (0, 1)],
}
START_DIRS = [(0, 1), (1, 0), (-1, 0), (-1, -1)]


def dfs(row, col, valid_dirs, visited):
    for d in valid_dirs:
        nr, nc = row + d[0], col + d[1]
        if nr >= 0 and nr < ROW_MAX and nc >= 0 and nc < COL_MAX:
            if grid[nr][nc] in PIPE_DIRS.keys() and (nr, nc) not in visited:
                visited.add((nr, nc))
                dfs(nr, nc, PIPE_DIRS[grid[nr][nc]], visited)


if __name__ == "__main__":
    print(part1())
