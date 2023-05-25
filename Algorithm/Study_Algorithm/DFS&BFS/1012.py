from collections import deque

import sys
sys.setrecursionlimit(10**6)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
inp = int(input())
def dfs(x, y):
    if x <= -1 or y <= -1 or x >= ymax or y >= xmax:
        return False
    if lis[x][y] == 1:
        lis[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False
from collections import deque
def bfs(x, y):
    q = deque([])
    q.append((x, y))
    lis[x][y] = 0
    while q:
        x, y = q.popleft()
        for t in range(4):
            nx = x+dx[t]
            ny = y+dy[t]
            if nx>=0 and ny>=0 and ny<xmax and nx<ymax and lis[nx][ny] == 1:
                q.append((nx, ny))
                lis[nx][ny] = 0
for _ in range(inp):
    cnt = 0
    xmax, ymax, case = map(int, input().split())
    lis = [[0] * xmax for _ in range(ymax)]
    for _ in range(case):
        y, x = map(int, input().split())
        lis[x][y] = 1
    for i in range(ymax):
        for z in range(xmax):
            if lis[i][z] == 1:
                bfs(i, z)
                cnt += 1
    print(cnt)