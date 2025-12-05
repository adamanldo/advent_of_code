data = str(open("input/8", "r").read())

width = 25
height = 6


def part1():
    layers = []
    p = 0
    while p < len(data):
        cur_layer = []
        for _ in range(height):
            cur_layer.append(data[p : p + width])
            p += width
        layers.append("".join(cur_layer))

    fewest_zeros = min(layers, key=lambda x: x.count("0"))
    print(fewest_zeros.count("1") * fewest_zeros.count("2"))


def print_full_image(layers):
    pixels = zip(*layers)
    line = ""
    c = 0
    for pixel in pixels:
        for p in pixel:
            if p == "0" or p == "1":
                if c >= width:
                    line += "\n"
                    c = 0
                if p == "0":
                    line += " "
                if p == "1":
                    line += "\u2588"
                c += 1
                break
    print(line)


def part2():
    layers = []
    p = 0
    while p < len(data):
        cur_layer = []
        for _ in range(height):
            cur_layer.append(data[p : p + width])
            p += width
        layers.append("".join(cur_layer))

    print_full_image(layers)


part2()
