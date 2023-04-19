import sys
input = sys.stdin.readline
inp = int(input())
lis = []
for _ in range(inp):
    lis.append(list(map(int, input().split())))
lis.sort(key=lambda x: (x[0], x[1]))
for i in range(len(lis)):
    print(*lis[i])
