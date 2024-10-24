from collections import defaultdict
graph = defaultdict(list)

with open('test/12', 'r') as f:
    for line in f.read().splitlines():
        s, e = line.split('-')
        graph[s].append(e)
        graph[e].append(s)

def dfs(current, visited):
    if visited[current] > 0:
        return 0
    if current == "end":
        return 1
    if current.islower():
        visited[current] += 1

    res = 0

    for node in graph[current]:
        if node != "start":
            res += dfs(node, visited)

    return res

def dfs2(current, visited, twice):
    if visited[current] > 0 and twice:
        return 0
    if current == "end":
        return 1
    if current.islower():
        visited[current] += 1
        if visited[current] == 2:
            twice = True

    res = 0

    for node in graph[current]:
        if node != "start":
            res += dfs2(node, visited, twice)

    visited[current] -= 1

    return res


def part1():
    print(dfs("start", defaultdict(int)))

def part2():
    print(dfs2("start", defaultdict(int), False))

part1()
part2()