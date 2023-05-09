from collections import deque
import sys
input = sys.stdin.readline
dz = [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]

def bfs(x, y):
    if lis[x][y] == 0:
        return False
    q = deque()
    lis[x][y] = 0
    q.append((x, y))
    while q:
        x, y = q.popleft()
        if x >= b or y >= a or x <= -1 or y <= -1:
            continue
        for nx, ny in dz:
            ndx = x + nx
            ndy = y + ny
            if ndx >= b or ndy >= a or ndx <= -1 or ndy <= -1:
                continue
            if lis[ndx][ndy] == 0:
                continue
            if lis[ndx][ndy] == 1:
                q.append((ndx, ndy))
                lis[ndx][ndy] = 0
    return True


while True:
    a, b = map(int, input().split())
    cnt = 0
    if a == 0 and b == 0:
        break
    lis = [list(map(int, input().split())) for _ in range(b)]
    for x in range(b):
        for y in range(a):
            if bfs(x, y):
                cnt += 1
    print(cnt)