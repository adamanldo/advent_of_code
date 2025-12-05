data = open('input/2', 'r').read().splitlines()

decrypt = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

def part_1():

    total = 0

    for line in data:
        opponent_move, my_move = line.split()

        if opponent_move == "A" and decrypt[my_move] == "A":
            total += 4
        if opponent_move == "A" and decrypt[my_move] == "B":
            total += 8
        if opponent_move == "A" and decrypt[my_move] == "C":
            total += 3
        if opponent_move == "B" and decrypt[my_move] == "A":
            total += 1
        if opponent_move == "B" and decrypt[my_move] == "B":
            total += 5
        if opponent_move == "B" and decrypt[my_move] == "C":
            total += 9
        if opponent_move == "C" and decrypt[my_move] == "A":
            total += 7
        if opponent_move == "C" and decrypt[my_move] == "B":
            total += 2
        if opponent_move == "C" and decrypt[my_move] == "C":
            total += 6
    
    print(total)

def get_move_and_score(opponent_move, desired_outcome):
    #rock
    if opponent_move == "A" and desired_outcome == "X":
        return 3 
    if opponent_move == "A" and desired_outcome == "Y":
        return 4 
    if opponent_move == "A" and desired_outcome == "Z":
        return 8 
    #paper
    if opponent_move == "B" and desired_outcome == "X":
        return 1
    if opponent_move == "B" and desired_outcome == "Y":
        return 5 
    if opponent_move == "B" and desired_outcome == "Z":
        return 9 
    #scissors
    if opponent_move == "C" and desired_outcome == "X":
        return 2 
    if opponent_move == "C" and desired_outcome == "Y":
        return 6 
    if opponent_move == "C" and desired_outcome == "Z":
        return 7 

def part_2():
    total = 0
    for line in data:
        opponent_move, desired_outcome = line.split()
        total += get_move_and_score(opponent_move, desired_outcome)
    print(total)

part_1()
part_2()