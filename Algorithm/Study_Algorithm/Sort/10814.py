import sys
input = sys.stdin.readline
inp = int(input())
lis = []
for _ in range(inp):
    a, b = input().split()
    a = int(a)
    lis.append((a, b))
lis.sort(key=lambda x : x[0])
for i in range(inp):
    print(*lis[i])
