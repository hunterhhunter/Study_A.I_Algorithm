import sys
input = sys.stdin.readline
inp = int(input())
lis = []
count = 1
for _ in range(inp):
    lis.append(tuple(map(int, input().split())))

lis.sort(key=lambda x: (x[1], x[0]))
x = lis[0][1]

for i in lis[1:]:
    if x <= i[0]:
        count += 1
        x = i[1]
print(count)

# while x < len(lis):
#     while lis[x][0] < lis[y][1]:
#         x += 1
#         if x >= len(lis):
#             break
#     y = x
#     count += 1