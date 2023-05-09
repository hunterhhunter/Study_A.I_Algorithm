from collections import deque
n, m = map(int, input().split())
lis = [list(map(int, input())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y): #미로 최단거리 찾기는 원점으로부터의 거리를 구하는 문제 -> 핵심
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        if x >= n or y >= m or x <= -1 or y <= -1:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or ny >= m or nx <= -1 or ny <= -1:
                continue
            if lis[nx][ny] == 0:
                continue
            if lis[nx][ny] == 1:
                q.append((nx, ny))
                lis[nx][ny] = lis[x][y] + 1 #이 코드가 핵심 -> 각 점이 원점으로부터의 거리를 기록
    return lis[-1][-1]

print(bfs(0, 0))