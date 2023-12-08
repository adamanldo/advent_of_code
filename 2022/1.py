data = open('input/1', 'r').read().split('\n\n')
calories_per_elf = []
for elf in data:
    calories_per_elf.append(sum([int(i) for i in elf.split('\n')]))

#part 1
def part1():
    print(max(calories_per_elf))

def part2():
    print(sum(sorted(calories_per_elf, reverse=True)[0:3]))

part1()
part2()