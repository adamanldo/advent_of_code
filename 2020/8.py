prog = [
    (x, int(y))
    for x, y in [line.split() for line in open("input/8").read().splitlines()]
]


def execute_program_stop_loop(prog):
    seen = set()
    acc = 0
    cur = 0
    while cur not in seen:
        seen.add(cur)
        op, arg = prog[cur]
        if op == "nop":
            cur += 1
        elif op == "acc":
            acc += arg
            cur += 1
        elif op == "jmp":
            cur += arg
    return acc


def execute_program(prog):
    seen = set()
    acc = 0
    cur = 0
    while cur not in seen and cur < len(prog):
        seen.add(cur)
        op, arg = prog[cur]
        if op == "nop":
            cur += 1
        elif op == "acc":
            acc += arg
            cur += 1
        elif op == "jmp":
            cur += arg
    if cur >= len(prog):
        return acc
    return None


def part1():
    return execute_program_stop_loop(prog)


def part2():
    # brute force: just try changing each instruction option then running the program
    for idx, line in enumerate(prog):
        op, arg = line
        if op == "acc":
            continue
        if op == "jmp":
            c = prog.copy()
            c[idx] = ("nop", arg)
        elif op == "nop":
            c = prog.copy()
            c[idx] = ("jmp", arg)

        p = execute_program(c)
        if p:
            return p


if __name__ == "__main__":
    print(part1())
    print(part2())
