grid = list(map(list, open("input/4").read().splitlines()))
mr, mc = len(grid), len(grid[0])

def accessible(r, c, grid):
    # up, right, down, left, up-right, down-right, down-left, up-left
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
    total_rolls = 0
    for d in dirs:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < mr and 0 <= nc < mc:
            if grid[nr][nc] == "@":
                total_rolls += 1
    
    return total_rolls < 4

def part1():
    total = 0
    for i in range(mr):
        for j in range(mc):
            if grid[i][j] == "@" and accessible(i, j, grid):
                total += 1
    
    return total

def part2():
    removed = 0
    any_accessible = True
    while any_accessible:
        for i in range(mr):
            for j in range(mc):
                if grid[i][j] == "@" and accessible(i, j, grid):
                    grid[i][j] = "."
                    removed += 1

        if not any((accessible(i, j, grid) and grid[i][j] == "@") for j in range(mc) for i in range(mr)): 
            any_accessible = False
        
    return removed

if __name__ == "__main__":
    print(part1())
    print(part2())