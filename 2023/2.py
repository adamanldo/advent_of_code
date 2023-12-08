games = open("input/2", "r").read().split("\n")


def part1():
    res = []
    dice = {"red": 12, "green": 13, "blue": 14}
    for game in games:
        gid, cubes = game.split(":")
        game_id = gid.split()[1]
        turns = [i.strip() for i in cubes.split(";")]
        possible = True
        for turn in turns:
            turn = [i.strip() for i in turns]
            for cube in turn:
                for turn in cube.strip().split(","):
                    num, color = turn.split()
                    if int(num) > dice[color]:
                        possible = False
        if possible == True:
            res.append(int(game_id))
    return sum(res)


def part2():
    res = 0
    for game in games:
        maximum_needed = {"red": 0, "blue": 0, "green": 0}
        cubes = game.split(":")[1]
        turns = [i.strip() for i in cubes.split(";")]
        for turn in turns:
            turn = [i.strip() for i in turns]
            for cube in turn:
                for turn in cube.strip().split(","):
                    num, color = turn.split()
                    num = int(num)
                    if num > int(maximum_needed[color]):
                        maximum_needed[color] = num
        power = 1
        for i in maximum_needed.values():
            power *= i
        res += power

    return res


if __name__ == "__main__":
    # print(part1())
    print(part2())
