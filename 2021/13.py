import numpy as np
import matplotlib.pyplot as plt

with open('input/13', 'r') as f:
    coords, instructions = f.read().split('\n\n')
    parsed_coords = []
    for cord in coords.split('\n'):
        for x, y in [cord.split(',')]:
            parsed_coords.append((int(x), int(y))) 
    instructions = instructions.split('\n')
    parsed_instructions = []
    for instruction in instructions:
        x = instruction.split()[2]
        y = x.split('=')
        parsed_instructions.append((y[0], int(y[1])))

visible_dots = set(parsed_coords)

def y_fold(y_coord, visible_dots):
    visible_dots_temp = visible_dots.copy()
    for (x, y) in visible_dots:
        if y > y_coord:
            visible_dots_temp.add((x, y_coord - (y - y_coord)))

    to_discard = list((x, y) for x, y in visible_dots_temp if y > y_coord)
    visible_dots_temp.difference_update(to_discard)
    return visible_dots_temp

def x_fold(x_coord, visible_dots):
    visible_dots_temp = visible_dots.copy()
    for (x, y) in visible_dots:
        if x > x_coord:
            visible_dots_temp.add((x_coord - (x - x_coord), y))

    to_discard = list((x, y) for x, y in visible_dots_temp if x > x_coord)
    visible_dots_temp.difference_update(to_discard)
    return visible_dots_temp

def part1():
    instruction = parsed_instructions[0]
    if instruction[0] == "x":
        x_fold(instruction[1])
    else:
        y_fold(instruction[1])
    print(len(visible_dots))

def part2(visible_dots):
    for instruction in parsed_instructions:
        if instruction[0] == "x":
            visible_dots = x_fold(instruction[1], visible_dots)
        else:
            visible_dots = y_fold(instruction[1], visible_dots)
    x, y = zip(*visible_dots)
    plt.scatter(x, y)
    plt.axis([-10,40,-10,8])
    plt.savefig("temp.png")


part2(visible_dots)
