from collections import deque
import sys
input = sys.stdin.readline
inp = int(input())
pic = [list(input()) for _ in range(inp)]
pic_for_sak = []
for i in range(inp):
    pic_for_sak.append(list(pic[i]))
    for x in range(inp):
        if pic_for_sak[i][x] == 'G':
            pic_for_sak[i][x] = 'R'
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0
cnt2 = 0
def bfs(lis, x, y):
    if lis[x][y] == '0':
        return False
    q = deque()
    q.append((x, y))
    while q:
        d = q.popleft()
        if d[0]>=inp or d[1]>=inp or d[0]<=-1 or d[1]<=-1 or lis[d[0]][d[1]] == '0':
            continue
        z = lis[d[0]][d[1]]
        lis[d[0]][d[1]] = '0'
        x, y = d[0], d[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=inp:
                nx = inp-1
            if ny>=inp:
                ny = inp-1
            if lis[nx][ny] == z:
                q.append((nx, ny))
    return True

for x in range(inp):
    for y in range(inp):
        if bfs(pic, x, y):
            cnt += 1
        if bfs(pic_for_sak, x, y):
            cnt2 += 1
print(cnt, cnt2)