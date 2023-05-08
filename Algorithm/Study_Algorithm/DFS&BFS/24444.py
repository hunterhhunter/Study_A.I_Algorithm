from collections import deque
import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
lis = [[] for _ in range(n+1)]
visit = [0] * (n+1)
cnt = 1
for _ in range(m):
    a, b = map(int, input().split())
    lis[a].append(b)
    lis[b].append(a)
for i in lis:
    i.sort()
lis2 = []
def bfs(start):
    global cnt
    q = deque()
    q.append(start)
    visit[start] = cnt
    while q:
        d = q.popleft()
        for x in lis[d]:
            if visit[x] == 0:
                cnt += 1
                visit[x] = cnt
                q.append(x)

bfs(r)
for i in visit[1:]:
    print(i)