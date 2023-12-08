with open('input/8', 'r') as f:
    signals = []
    outputs = []
    parse = [line.split(' | ') for line in f.read().split('\n')]
    for i in range(len(parse)):
        signals.append(parse[i][0])
        outputs.append(parse[i][1])

def contains_any(s1, s2):
    for c in s2:
        if c in s1:
            return True
    return False

def contains_all(s1, s2):
    for c in s2:
        if c not in s1:
            return False
    return True

def part1(outputs):
    unique = {2, 4, 3, 7}
    res = 0
    for line in outputs:
        for signal in line.split():
            if len(signal) in unique:
                res += 1

    print(res)

def part2(signals, outputs):
    out = []
    for i in range(len(signals)):
        c = signals[i].split()
        character_signal_map = {}
        for s in c:
            if len(s) == 2:
                character_signal_map[1] = s
            elif len(s) == 4:
                character_signal_map[4] = s
            elif len(s) == 3:
                character_signal_map[7] = s
            elif len(s) == 7:
                character_signal_map[8] = s
        c = [i for i in c if i not in character_signal_map.values()]
        for s in c:
            if len(s) == 6 and not contains_all(s, character_signal_map[1]):
                character_signal_map[6] = s
                c.remove(s)
        for s in c:
            if len(s) == 6 and (not contains_all(s, character_signal_map[4])):
                character_signal_map[0] = s
                c.remove(s)
        for s in c:
            if len(s) == 6:
                character_signal_map[9] = s
                c.remove(s)
        for s in c:
            if not contains_all(character_signal_map[9], s):
                character_signal_map[2] = s
                c.remove(s)
        for s in c:
            if not contains_all(s, character_signal_map[1]):
                character_signal_map[5] = s
                c.remove(s)
        character_signal_map[3] = c[0]
        reverse_char_map = {v: k for k, v in character_signal_map.items()}
        res = ''
        for output in outputs[i].split():
            for char in reverse_char_map:
                if len(output) == len(char): 
                    if contains_all(output, char):
                        res += str(reverse_char_map[char])
        out.append(int(res))

    print("Total: " + str(sum(out)))

        

part2(signals, outputs)