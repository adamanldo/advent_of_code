data = open('input/6', 'r').read().split(',')
data = [int(i) for i in data]

days = 256

state = data

def part1(state, days):
    for _ in range(days):
        print("day " + str(_))
        new_fish = 0
        for idx, val in enumerate(state):
            if val == 0:
                new_fish += 1
                state[idx] = 6
            else:
                state[idx] -= 1
        for _ in range(new_fish):
            state.append(8)
        #print("day: " + str(day) + ": " + "state: " + str(state))

    print(len(state))

def part2(state, days):
    d = {}
    for _ in range(9):
        d[_] = 0
    for fish in state:
        d[fish] += 1
    #print("initial state : " + str(d))
    for _ in range(days):
        new_fish = 0
        fish_resets = 0
        for day in d:
            if day == 0:
                new_fish += d[day]
                fish_resets += d[day]
            else:
                d[day - 1] = d[day]
        d[8] = new_fish
        d[6] += fish_resets
        #print("day : " + str(_ + 1) + ": " + "state: " + str(d))
    print(sum([fish for fish in d.values()]))

part2(state, days)