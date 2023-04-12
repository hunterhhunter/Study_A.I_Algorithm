inp = int(input())
lis = []
for _ in range(inp):
    lis.append(list(map(int, input().split())))

x = [r[0] for r in lis]
y = [r[1] for r in lis]

print((max(x) - min(x)) * (max(y) - min(y)))