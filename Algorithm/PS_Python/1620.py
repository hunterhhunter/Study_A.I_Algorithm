import sys
input = sys.stdin.readline
a, b = map(int, input().split())
lis1 = dict()
lis2 = dict()
for i in range(1, a+1):
    z = input().rstrip()
    lis1[z] = i
    lis1[i] = z
for _ in range(b):
    c = input().rstrip()
    if c.isdigit():
        print(lis1[int(c)])
    else:
        print(lis1[c])