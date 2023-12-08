from collections import defaultdict
graph = defaultdict(list)

with open('input/12', 'r') as f:
    for line in f.read().splitlines():
        s, e = line.split('-')
        graph[s].append(e)
        graph[e].append(s)

def dfs(current, visited, twice):
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
            res += dfs(node, visited, twice)

    visited[current] -= 1

    return res

print(dfs("start", defaultdict(int), False))