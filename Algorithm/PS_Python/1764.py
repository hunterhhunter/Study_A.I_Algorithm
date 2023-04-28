import sys
input = sys.stdin.readline
a, b = map(int, input().split())
listen = set(input() for _ in range(a))
see = set(input() for _ in range(b))
cnt = 1
result = sorted(list(listen | see))
print(len(result))
result.sort()
for i in result:
    print(i, end='')