data = open('input/8', 'r').read().splitlines()

row_max = len(data)
col_max = len(data[0])

def check_visibility(row_idx, col_idx):
    h = data[row_idx][col_idx]

    #if on edge return visible
    if row_idx == 0 or row_idx == row_max-1 or col_idx == 0 or col_idx == col_max-1:
        return True

    #check left
    if all([data[row_idx][i] < h for i in range(0, col_idx)]):
        return True

    #check right
    if all([data[row_idx][i] < h for i in range(col_idx + 1, col_max)]):
        return True

    #check upwards
    if all([data[i][col_idx] < h for i in range(0, row_idx)]):
        return True

    #check down
    if all([data[i][col_idx] < h for i in range(row_idx+1, row_max)]):
        return True
    
    return False

def get_scenic_score(row_idx, col_idx):
    h = data[row_idx][col_idx]
    scenic_score = 1

    #get all trees with a score of the height or greater, then get the one with the minimum distance away
    #add the distance to the scenic score
    #if no trees, return the distance between it and the edge in that direction 

    #if on edge ignore, one of viewing distances will be zero
    if row_idx == 0 or row_idx == row_max-1 or col_idx == 0 or col_idx == col_max-1:
        return 0

    #check left
    blocking_trees = [(row_idx, i) for i in range(0, col_idx) if data[row_idx][i] >= h]
    if len(blocking_trees) < 1:
        if col_idx > 0:
            scenic_score *= col_idx
    else:
        closest_tree = min([abs(col_idx - col) for (_, col) in blocking_trees])
        scenic_score *= closest_tree

    #check right
    blocking_trees = [(row_idx, i) for i in range(col_idx + 1, col_max) if data[row_idx][i] >= h]
    if len(blocking_trees) < 1:
        scenic_score *= (col_max - 1) - col_idx
    else:
        closest_tree = min([abs(col_idx - col) for (_, col) in blocking_trees])
        scenic_score *= closest_tree
    
    #check up
    blocking_trees = [(i, col_idx) for i in range(0, row_idx) if data[i][col_idx] >= h]
    if len(blocking_trees) < 1:
        if row_idx > 0:
            scenic_score *= row_idx
    else:
        closest_tree = min([abs(row_idx - row) for (row, _) in blocking_trees])
        scenic_score *= closest_tree

    #check down
    blocking_trees = [(i, col_idx) for i in range(row_idx+1, row_max) if data[i][col_idx] >= h]
    if len(blocking_trees) < 1:
        scenic_score *= (row_max - 1) - row_idx
    else:
        closest_tree = min([abs(row_idx - row) for (row, _) in blocking_trees])
        scenic_score *= closest_tree

    return scenic_score

    
def part_1():
    count = 0
    for i in range(row_max):
        for j in range(col_max):
            if check_visibility(i, j):
                count += 1
    print(count)

def part_2():
    highest_scenic_score = 0
    for i in range(row_max):
        for j in range(col_max):
            scenic_score = get_scenic_score(i, j)
            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score 

    print(highest_scenic_score)

part_1()
part_2()