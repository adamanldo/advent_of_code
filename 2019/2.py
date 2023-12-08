from copy import deepcopy


program = [int(i) for i in (open("input/2", "r").read().split(","))]


def part1():
    program[1] = 12
    program[2] = 2
    print(process(program)[0])


def part2():
    for inp1 in range(100):
        for inp2 in range(100):
            program_attempt = deepcopy(program)
            program_attempt[1] = inp1
            program_attempt[2] = inp2
            if process(program_attempt)[0] == 19690720:
                return 100 * inp1 + inp2


def process(program):
    index = 0
    while True:
        if index >= len(program) - 1:
            return program
        elif program[index] == 99:
            return program
        elif program[index] == 1:
            position_1 = program[index + 1]
            position_2 = program[index + 2]
            output_position = program[index + 3]
            program[output_position] = program[position_1] + program[position_2]

            index += 4

        elif program[index] == 2:
            position_1 = program[index + 1]
            position_2 = program[index + 2]
            output_position = program[index + 3]
            program[output_position] = program[position_1] * program[position_2]

            index += 4


if __name__ == "__main__":
    # part1()
    print(part2())
