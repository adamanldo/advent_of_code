from collections import deque
data = open('input/4', 'r').read().strip().split("\n\n")

numbers = deque([int(x) for x in data.pop(0).split(",")])

boards = []
for board in data:
    rows = [[int(x) for x in row.split()] for row in board.split('\n')]
    boards.append(rows)

def has_won(board, called_numbers):
    return any(all(num in called_numbers for num in line) for line in [*board, *zip(*board)])

def score(board, called_numbers, last_number):
    return last_number * sum(num for line in board for num in line if num not in called_numbers)

def part1():
    called_numbers = set()
    while numbers:
        num = numbers.popleft()
        called_numbers.add(num)
        for board in boards:
            if has_won(board, called_numbers):
                return score(board, called_numbers, num)

#print(part1())

def part2(numbers, boards):
    called_numbers = set()
    while numbers:
        num = numbers.popleft()
        called_numbers.add(num)
        if len(boards) == 1 and has_won(boards[0], called_numbers):
            return score(boards[0], called_numbers, num)
        boards = [board for board in boards if not has_won(board, called_numbers)] 

print(part2(numbers, boards))


                    


