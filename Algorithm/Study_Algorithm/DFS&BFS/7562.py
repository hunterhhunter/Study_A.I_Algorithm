from collections import deque
import sys
input = sys.stdin.readline
inp = int(input())
dz = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1,-2), (2, -1), (2, 1), (1, 2)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        if x == target_x and y == target_y:
            return maping[x][y]
        for dx, dy in dz:
            nx = x + dx
            ny = y + dy
            if nx <= -1 or ny <= -1 or nx >= square or ny >= square:
                continue
            if maping[nx][ny] != 0:
                continue
            if maping[nx][ny] == 0:
                maping[nx][ny] = maping[x][y] + 1
                q.append((nx, ny))
for _ in range(inp):
    square = int(input())
    maping = [[0]*square for _ in range(square)]
    now_x, now_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    print(bfs(now_x, now_y))