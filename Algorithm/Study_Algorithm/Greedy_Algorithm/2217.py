import sys
input = sys.stdin.readline
inp = int(input())
lis = []
for _ in range(inp):
    lis.append(int(input()))
mid = sum(lis) // len(lis)
lis2 = [i for i in lis if i >= mid]
lis2.sort()
print(len(lis2) * lis2[0])