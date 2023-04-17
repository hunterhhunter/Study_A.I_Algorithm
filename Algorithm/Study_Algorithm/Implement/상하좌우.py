inp = int(input())
lis = list(map(str, input().split()))
ho = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
x, y = 1, 1

for i in lis:
    for z in range(len(ho)):
        if i == ho[z]:
            nx = dx[z] + x
            ny = y + dy[z]
    if nx < 1 or nx < 1 or nx > inp or ny > inp:
        continue
    x, y = nx, ny
print(x, y)

# for i in lis:
#     if i == 'R':
#         if x == inp-1:
#             pass
#         else:
#             x += 1
#     elif i == 'L':
#         if x == 0:
#             pass
#         else:
#             x -= 1
#     elif i == 'U':
#         if y == 0:
#             pass
#         else:
#             y -= 1
#     elif i == 'D':
#         if y == inp - 1:
#             pass
#         else:
#             y += 1
# print(y+1, x+1)