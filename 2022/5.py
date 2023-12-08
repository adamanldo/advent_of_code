raw_crates, raw_instructions = open('input/5', 'r').read().split('\n\n')

instructions = []

#push each instruction onto a stack
for line in reversed(raw_instructions.splitlines()):
    line = line.replace('move ', ' ')
    line = line.replace(' from ', ' ')
    line = line.replace(' to ', ' ')
    instructions.append(list(int(x) for x in line.split()))

stacks = []

for _ in range(9):
    stacks.append([])

#just hardcode the index of each stack of crates
stack_to_index = {
    1: 1,
    2: 5,
    3: 9,
    4: 13,
    5: 17,
    6: 21,
    7: 25,
    8: 29,
    9: 33
}

c = reversed(raw_crates.splitlines())
next(c)

for line in c:
    for k in stack_to_index:
        if line[stack_to_index[k]].isalpha():
            stacks[k - 1].append(line[stack_to_index[k]])

def execute_9000_crate_instruction(l):
    num_crates_to_move = l[0]
    start_stack = l[1] - 1
    end_stack = l[2] - 1

    for _ in range(num_crates_to_move):
        crate = stacks[start_stack].pop()
        stacks[end_stack].append(crate)

def execute_9001_crate_instruction(l):
    num_crates_to_move = l[0]
    start_stack = l[1] - 1
    end_stack = l[2] - 1

    temp_stack = []

    for _ in range(num_crates_to_move):
        crate = stacks[start_stack].pop()
        temp_stack.append(crate)
    
    while (temp_stack):
        crate = temp_stack.pop()
        stacks[end_stack].append(crate)

def part_1():
    while(instructions):
        instruction = instructions.pop()
        execute_9000_crate_instruction(instruction)
    res = ''.join([stacks[i][-1] for i in range(9)])
    print(res)

def part_2():
    while(instructions):
        instruction = instructions.pop()
        execute_9001_crate_instruction(instruction)
    res = ''.join([stacks[i][-1] for i in range(9)])
    print(res)

#part_1()
part_2()
