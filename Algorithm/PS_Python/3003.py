inp = input().split()
goal = [1, 1, 2, 2, 2, 8]
lis = []
for i in range(len(inp)):
    lis.append(goal[i] - int(inp[i]))

print(*lis)