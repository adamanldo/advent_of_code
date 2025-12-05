data = open("input/2").read().split(",")
ranges = [tuple(map(int, entry.split('-'))) for entry in data]

def part1():
    total = 0
    for entry in ranges:
        f, s = entry
        for num in range(f, s+1):
            string_int = str(num)
            m = len(string_int) // 2
            s1, s2 = string_int[0:m], string_int[m:]
            if s1 == s2:
                total += num

    return total

def part2():
    total = 0
    for entry in ranges:
        f, s = entry
        for num in range(f, s+1):
            string_int = str(num)
            if does_only_repeated_substr_exist(string_int):
                total += num

    return total

def does_only_repeated_substr_exist(entry):
    d = set()
    for i in range(len(entry)):
        for j in range(i, len(entry)):
            substr = entry[i:j+1]
            if substr in d and all_substrings_match(entry, substr):
                return True
            else:
                d.add(substr)
    return False

def all_substrings_match(entry, substr):
    n = len(substr)
    for i in range(0, len(entry), n):
        if entry[i:i+n] != substr:
            return False
    return True

if __name__ == "__main__":
    print(part1())
    print(part2())