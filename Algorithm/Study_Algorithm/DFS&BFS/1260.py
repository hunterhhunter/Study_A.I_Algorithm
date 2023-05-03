from collections import deque
num, line, start = map(int, input().split())
lis = [[] for _ in range(num + 1)]
for _ in range(line):
    a, b = map(int, input().split())
    lis[a].append(b)
    lis[b].append(a)
for i in lis:
    i.sort()
visited = [False] * (num+1)
def dfs(start, lis):
    visited[start] = True
    print(start, end=' ')
    for i in lis[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i, lis)
dfs(start, lis)
print()
visited2 = [False] * (num+1)

def bfs(lis, start):
    queue = deque([start])
    visited2[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in lis[v]:
            if not visited2[i]:
                queue.append(i)
                visited2[i] = True
bfs(lis, start)