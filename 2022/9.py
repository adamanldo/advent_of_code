data = open('test/9', 'r').read().splitlines()

dirs = {
    "U" : (0, 1), 
    "D": (0,-1),
    "L": (-1,0),
    "R": (1,0),
    "UR": (1, 1),
    "DR": (1, -1),
    "DL": (-1, -1),
    "UL": (-1, 1)
}


def part_1():

    t_positions = set()

    h = (0, 0)
    t = (0, 0)

    h_prev = None
    t_positions.add((0, 0))

    for line in data:
        d, num = line.split()
        num = int(num)

        for _ in range(num):
            x, y = dirs[d]
            h = (h[0] + x, h[1] + y)

            #move the tail if its gotten two squares away
            in_range = False
            for d_d in dirs:
                d_x = dirs[d_d][0]
                d_y = dirs[d_d][1]
                if t == (h[0] + d_x, h[1] + d_y):
                    in_range = True

            #check if h is on t
            if t == h:
                in_range = True

            if not in_range:
                t_positions.add(h_prev)
                t = h_prev

            h_prev = h

    print(len(t_positions))

def part_2():

    knot_positions = {}

    h = (0, 0)
    # all knots excluding head
    for i in range(1, 10):
        knot_positions[i] = (0, 0)

    for line in data:
        d, num = line.split()
        num = int(num)

        for _ in range(num):
            x, y = dirs[d]
            h = (h[0] + x, h[1] + y)

            #move each knot if the knot before it has moved two squares away
            for i in range(1, 9):
                in_range = False

                #check every adjacent square to see if the previous knot is in range
                for d_d in dirs:
                    d_x = dirs[d_d][0]
                    d_y = dirs[d_d][1]
                    if t == (h[0] + d_x, h[1] + d_y):
                        in_range = True

                #check if h is on t
                if t == h:
                    in_range = True

                if not in_range:
                    t_positions.add(h_prev)
                    t = h_prev

                h_prev = h

    print(len(t_positions))

#part_1()
part_2()