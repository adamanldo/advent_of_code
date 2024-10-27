program = [int(i) for i in (open("test/5", "r").read().split(","))]


def part1():
    print(run(program))


def process_instruction(program, opcode_index, parameter_mode):

    return program


def run(program):
    ip = 0
    while True:
        if ip >= len(program) - 1:
            return program
        elif program[ip] == 99:
            return program
        else:
            instruction = [int(x) for x in program[ip]]
            instruction_type = instruction[-1]
            for _ in range(2):
                instruction.pop()
            parameter_1_mode = instruction.pop()
            parameter_2_mode = instruction.pop()
            parameter_3_mode = instruction.pop()

            if instruction_type == 1:
                count = 0
                while count < 4: 
                if parameter_1_mode == 0:
                    program 
                program[output_position] = program[position_1] + program[position_2]

            elif instruction_type == 2:
                program[output_position] = program[position_1] * program[position_2]

            elif instruction_type == 3:
                program[output_position] = program[position_1] * program[position_2]
            index += 4


if __name__ == "__main__":
    part1()
