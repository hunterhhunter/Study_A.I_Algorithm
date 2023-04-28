import sys
input = sys.stdin.readline
inp = int(input())
lis = list(map(int, input().split()))
lis1 = sorted(set(lis))
result = {}

for i in range(len(lis1)):
    result[lis1[i]] = i
for i in lis:
    print(result[i], end=' ')
