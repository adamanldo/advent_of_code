data = open('input/4', 'r').read().splitlines()

def part_1():
    contains = 0
    for pairs in data:

        first, second = pairs.split(',')
        first_start, first_end = tuple(int(x) for x in first.split('-'))
        second_start, second_end = tuple(int(x) for x in second.split('-'))
        if (first_start <= second_start and first_end >= second_end) or (second_start <= first_start and second_end >= first_end):
            contains += 1

    print(contains)

def part_2():
    overlaps= 0
    for pairs in data:

        first, second = pairs.split(',')
        first_start, first_end = tuple(int(x) for x in first.split('-'))
        second_start, second_end = tuple(int(x) for x in second.split('-'))

        if (first_end >= second_start and second_end >= first_start):
            overlaps += 1

    print(overlaps)
    
part_1()
part_2()
        