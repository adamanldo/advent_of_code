from collections import Counter


word_search = open("input/4").read().splitlines()

mr, mc = len(word_search), len(word_search[0])


def check_xmas(i, j, word_search):
    dirs = [(1, 0), (0, -1), (0, 1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    total = 0

    for d in dirs:
        is_xmas = True
        dx, dy = d
        for xmas_idx, letter in enumerate("XMAS"):
            ii = i + xmas_idx * dx
            jj = j + xmas_idx * dy
            if not (0 <= ii < mr and 0 <= jj < mc):
                is_xmas = False
                break
            if word_search[ii][jj] != letter:
                is_xmas = False
                break
        if is_xmas:
            total += 1

    return total


def check_x_mas(i, j, word_search):
    # down right, up left, down left, up right
    dirs = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    is_x_mas = True
    diags = {}

    for d in dirs:
        dx, dy = d
        ii = i + dx
        jj = j + dy
        if not (0 <= ii < mr and 0 <= jj < mc):
            return False
        diags[d] = word_search[ii][jj]

    c = Counter(diags.values())
    if c["M"] != 2 or c["S"] != 2:
        return False
    if diags[(-1, -1)] == diags[(1, 1)] or diags[(1, -1)] == diags[(-1, 1)]:
        return False

    return is_x_mas


def part1():
    res = 0
    for i in range(len(word_search)):
        for j in range(len(word_search[0])):
            if word_search[i][j] == "X":
                res += check_xmas(i, j, word_search)
    return res


def part2():
    res = 0
    for i in range(len(word_search)):
        for j in range(len(word_search[0])):
            if word_search[i][j] == "A":
                if check_x_mas(i, j, word_search):
                    res += 1
    return res


if __name__ == "__main__":
    print(part1())
    print(part2())
