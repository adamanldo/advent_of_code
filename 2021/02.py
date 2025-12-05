data = open('input/2', 'r').read().splitlines()

hor = 0
ver = 0

for i in data:
    t = i.split()
    if t[0] == "forward":
        hor += int(t[1])
    elif t[0] == "down":
        ver += int(t[1])
    else:
        ver -= int(t[1])

print(ver * hor)

hor2 = 0
depth = 0
aim = 0

for i in data:
    t = i.split()
    if t[0] == "down":
        aim += int(t[1])
    elif t[0] == "up":
        aim -= int(t[1])
    else:
        hor2 += int(t[1])
        depth += int(t[1]) * aim

print(hor2 * depth)