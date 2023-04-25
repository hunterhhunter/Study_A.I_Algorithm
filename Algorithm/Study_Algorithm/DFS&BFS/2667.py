inp = int(input())
sol = []
lis = []
for _ in range(inp):
    lis.append(list(map(int, input())))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count = 0
result = 0

def solution(x, y):
    global count
    if x <= -1 or y <= -1 or x >= inp or y >= inp:
        return False
    if lis[x][y] == 1:
        count += 1
        lis[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            solution(nx, ny)
        return True
    return False

for x in range(inp):
    for y in range(inp):
        if solution(x, y):
            sol.append(count)
            result += 1
            count = 0
sol.sort()
print(result)
for i in sol:
    print(i)
