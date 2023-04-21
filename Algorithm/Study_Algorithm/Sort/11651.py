import sys
input = sys.stdin.readline
inp = int(input())
lis = []
for _ in range(inp):
    lis.append(list(map(int, input().split())))
lis.sort(key=lambda x: (x[1], x[0]))
for i in range(inp):
    print(*lis[i])