lis = [list(map(int, input().split())) for _ in range(9)]
max1 = 0
x, y = 0, 0
for i in range(9):
    if max1 < max(*lis[i], max1):
        max1 = max(*lis[i], max1)
        x = i

y = lis[x].index(max1)

print(max1)
print(x+1, y+1)