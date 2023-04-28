import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
connections = [[] for _ in range(n)]
visited = [False] * n
cnt = 0
for _ in range(m):
    a, b = map(int, input().split())
    connections[a-1].append(b)
    connections[b-1].append(a)
def dfs(i):
    visited[i] = True
    for f in connections[i]:
        if not visited[f-1]:
            dfs(f-1)
for i in range(n):
    if not visited[i]:
        if not connections[i]:
            cnt += 1
            visited[i] = True
        else:
            dfs(i)
            cnt += 1
print(cnt)
