data = str(open("input/8", "r").read())


def part1():
    width = 25
    height = 6
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


part1()
