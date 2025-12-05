data = open('input/3', 'r').read().splitlines()

priorities = {}

count = 1
for c in range(ord('a'), ord('z') + 1):
    priorities[chr(c)] = count
    count += 1

count = 27
for c in range(ord('A'), ord('Z') + 1):
    priorities[chr(c)] = count
    count += 1

def part_1():
    total = 0

    for line in data:
        m = len(line) // 2
        first_half = set(line[0:m])
        second_half = line[m:len(line)]

        common_letter = ''
        for letter in second_half:
            if letter in first_half:
                common_letter = letter
                break
        total += priorities[common_letter]
    
    print(total)

def part_2():
    total = 0

    for num in range(0, len(data), 3):
        elf_1 = set(data[num])
        elf_2 = set(data[num+1])
        for letter in data[num+2]:
            if letter in elf_1 and letter in elf_2:
                common_letter = letter
        
        total += priorities[common_letter]
    
    print(total)
        
part_1()
part_2()
