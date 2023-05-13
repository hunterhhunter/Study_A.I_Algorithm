from collections import deque
z, i = map(int, input().split())
lis = [list(map(int, input().split())) for _ in range(z)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
wid = []
result = 0
def bfs(x, y):
    cnt = 0
    q = deque()
    q.append((x, y))
    lis[x][y] = 0
    while q:
        cnt += 1
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx >= z or ny >= i or nx <= -1 or ny <= -1:
                continue
            if lis[nx][ny] != 1:
                continue
            if lis[nx][ny] == 1:
                q.append((nx, ny))
                lis[nx][ny] = 0
    wid.append(cnt)

for x in range(z):
    for y in range(i):
        if lis[x][y] == 1:
            bfs(x, y)
            result += 1
print(result)
print(max(wid) if wid else 0)