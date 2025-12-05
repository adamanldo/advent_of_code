wires = [i for i in (open("input/3", "r").read().split("\n"))]


def part1():
    wire_paths = []
    for path in wires:
        current = (0, 0)
        wire_path = set()
        segments = path.split(",")
        for segment in segments:
            direction, distance = segment[0], int(segment[1:])
            for _ in range(distance):
                if direction == "U":
                    move = (current[0] + 1, current[1])
                    wire_path.add(move)
                elif direction == "D":
                    move = (current[0] - 1, current[1])
                    wire_path.add(move)
                elif direction == "L":
                    move = (current[0], current[1] - 1)
                    wire_path.add(move)
                elif direction == "R":
                    move = (current[0], current[1] + 1)
                    wire_path.add(move)
                current = move

        wire_paths.append(wire_path)

    intersections = list(set.intersection(*wire_paths))
    manhattan_distances = []
    for i in intersections:
        md = manhattan_distance((0, 0), i)
        manhattan_distances.append(md)

    return min(manhattan_distances)


def part2():
    wire_paths = []
    all_distances = []
    for path in wires:
        current = (0, 0)
        wire_path = set()
        distances = {}
        move_total = 0
        segments = path.split(",")
        for segment in segments:
            direction, distance = segment[0], int(segment[1:])
            for _ in range(distance):
                if direction == "U":
                    move = (current[0] + 1, current[1])
                    wire_path.add(move)
                    move_total += 1
                    if move not in distances:
                        distances[move] = move_total
                elif direction == "D":
                    move = (current[0] - 1, current[1])
                    wire_path.add(move)
                    move_total += 1
                    if move not in distances:
                        distances[move] = move_total
                elif direction == "L":
                    move = (current[0], current[1] - 1)
                    wire_path.add(move)
                    move_total += 1
                    if move not in distances:
                        distances[move] = move_total
                elif direction == "R":
                    move = (current[0], current[1] + 1)
                    wire_path.add(move)
                    move_total += 1
                    if move not in distances:
                        distances[move] = move_total
                current = move

        wire_paths.append(wire_path)
        all_distances.append(distances)

    intersections = list(set.intersection(*wire_paths))
    first_wire_distances = all_distances[0]
    second_wire_distances = all_distances[1]

    m = 1000000
    for i in intersections:
        s1 = first_wire_distances[i]
        s2 = second_wire_distances[i]
        if s1 + s2 < m:
            m = s1 + s2

    return m


def manhattan_distance(p1: tuple, p2: tuple) -> int:
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


if __name__ == "__main__":
    # print(part1())
    print(part2())
