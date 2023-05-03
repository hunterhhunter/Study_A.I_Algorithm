import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n, m, r = map(int, input().split())
visit = [0] * (n+1)
lis = [[] for _ in range(n+1)]
cnt = 1

for _ in range(m):
    a, b = map(int, input().split())
    lis[a].append(b)
    lis[b].append(a)
for i in lis:
    i.sort(reverse=True)

def dfs(start, lis):
    global cnt
    visit[start] = cnt
    for i in lis[start]:
        if visit[i] == 0:
            cnt += 1
            dfs(i, lis)
dfs(r, lis)
for i in range(1, n+1):
    print(visit[i])