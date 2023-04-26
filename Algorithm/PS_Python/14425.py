import sys
input = sys.stdin.readline
a, b = map(int, input().split())

lis1 = set(input() for _ in range(a))
lis2 = list(input() for _ in range(b))

cnt = 0
for x in lis2:
    if x in lis1:
        cnt += 1
print(cnt)