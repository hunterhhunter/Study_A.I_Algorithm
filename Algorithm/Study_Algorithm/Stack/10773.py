import sys
input = sys.stdin.readline
inp = int(input())
lis = []
for _ in range(inp):
    a = int(input())
    if a != 0:
        lis.append(a)
    else:
        lis.pop()
print(sum(lis))