database = open("input/5").read().split("\n\n")
fresh_ingredients = [tuple(map(int, id_range.split("-"))) for id_range in database[0].split()]
available_ingredients = [int(i) for i in database[1].splitlines()]

def part1():
    total_fresh = 0
    for ing_id in available_ingredients:
        fresh = False
        for lower, upper in fresh_ingredients:
            if lower <= ing_id <= upper:
                fresh = True
        
        if fresh:
            total_fresh += 1

    return total_fresh

def part2():
    fresh_ingredients.sort()
    merged = []
    for lower, upper in fresh_ingredients:
        if not merged or merged[-1][1] < lower:
            merged.append([lower, upper])
        else:
            merged[-1][1] = max(merged[-1][1], upper)

    total_fresh = 0
    for lower, upper in merged:
        total_fresh += upper - lower + 1
    
    return total_fresh

def main():
    print("Part 1:", part1())
    print("Part 2:", part2())

if __name__ == "__main__":
    main()
