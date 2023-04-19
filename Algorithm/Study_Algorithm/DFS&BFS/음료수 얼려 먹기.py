n, m = map(int, input().split())

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

graph =[]
for _ in range(n):
    graph.append(list(map(int, input())))
result = 0
for i in range(n):
    for z in range(m):
        if dfs(i, z):
            result += 1

print(result)
