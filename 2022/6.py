data = open('input/6', 'r').read()

def solve(size):
    start, end = 0, size

    while end <= len(data):
        duplicates = False
        s = set()
        for l in data[start:end]:
            if l in s:
                duplicates = True
                break
            s.add(l)
        if duplicates == False:
            print(end)
            break
        start += 1
        end += 1

solve(4)
solve(14)