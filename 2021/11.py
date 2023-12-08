with open('input/11', 'r') as f:
    octopi = [[int(i) for i in line] for line in f.read().splitlines()]

ROW_MAX = len(octopi)
COL_MAX = len(octopi[0])

def find_adjacent_octopi(row, col):
    adjacent_octopi = []
    #left
    if col > 0:
        adjacent_octopi.append((row, col - 1)) 
    #right
    if col < COL_MAX - 1:
        adjacent_octopi.append((row, col + 1))
    #top
    if row > 0:
        adjacent_octopi.append((row - 1, col))
    #bottom
    if row < COL_MAX - 1:
        adjacent_octopi.append((row + 1, col))
    #upper left
    if row > 0 and col > 0:
        adjacent_octopi.append((row - 1, col - 1))
    #upper right
    if row > 0 and col < COL_MAX - 1:
        adjacent_octopi.append((row - 1, col + 1))
    #lower left
    if row < ROW_MAX - 1 and col > 0:
        adjacent_octopi.append((row + 1, col - 1))
    #lower right
    if row < ROW_MAX - 1 and col < COL_MAX - 1:
        adjacent_octopi.append((row + 1, col + 1))
    return adjacent_octopi

def flash(row, col, flashed):
    octopi[row][col] += 1
    flashed[row][col] = 1
    for adj in find_adjacent_octopi(row, col):
        octopi[adj[0]][adj[1]] += 1
        if octopi[adj[0]][adj[1]] > 9 and flashed[adj[0]][adj[1]] == 0:
            flash(adj[0], adj[1], flashed)


total_flashes = 0

for _ in range(10000):
    #increase energy
    for row in range(ROW_MAX):
        for col in range(COL_MAX):
            octopi[row][col] += 1
    
    #check for flashes
    flashed = [[0 for i in range(COL_MAX)] for j in range(ROW_MAX)]
    for row in range(ROW_MAX):
        for col in range(COL_MAX):
            if octopi[row][col] > 9 and flashed[row][col] == 0:
                flash(row, col, flashed)

    #check for simultaneous flash
    all_flashed = True
    for row in range(ROW_MAX):
        for col in range(COL_MAX):
            if flashed[row][col] != 1:
                all_flashed = False
    
    if all_flashed == True:
        print(f"All flashed on step {_ + 1}")
        break

    #set flashed octopi to 0
    for row in range(ROW_MAX):
        for col in range(COL_MAX):
            if octopi[row][col] > 9:
                octopi[row][col] = 0

    #use flashed array to increase total number of flashes
    for row in range(ROW_MAX):
        for col in range(COL_MAX):
            if flashed[row][col] == 1:
                total_flashes += 1

print(total_flashes)


