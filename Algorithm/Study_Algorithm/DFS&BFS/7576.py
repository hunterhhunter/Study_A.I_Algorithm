from collections import deque
n, m = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
lis = [list(map(int, input().split())) for _ in range(m)]
start_1 = []
maxq = 0
for x in range(m):
    for y in range(n):
        if lis[x][y] == 1:
            start_1.append((x, y))
def bfs():
    q = deque()
    for i in start_1:
        q.append(i)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= m or ny >= n or nx <= -1 or ny <= -1:
                continue
            if lis[nx][ny] == 1 or lis[nx][ny] == -1:
                continue
            if lis[nx][ny] == 0:
                lis[nx][ny] = lis[x][y] + 1
                q.append((nx, ny))
def check():
    global maxq
    for i in lis:
        for z in i:
            if z > maxq:
                maxq = z
        if 0 in i:
            return False
    return True

bfs()

if check():
    print(maxq - 1)
else:
    print(-1)