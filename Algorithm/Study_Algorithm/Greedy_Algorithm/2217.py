import sys
input = sys.stdin.readline
inp = int(input())
lis = []
for _ in range(inp):
    lis.append(int(input()))
lis.sort(reverse=True)
lis2 = []
for i in range(inp):
    lis2.append(lis[i] * (i+1))
print(max(lis2))