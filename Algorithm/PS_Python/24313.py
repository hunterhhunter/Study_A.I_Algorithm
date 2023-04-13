a, b = map(int, input().split())
c = int(input())
d = int(input())

flag = True
for n in range(d, 101):
    if a * n + b > c * n:
        flag = False

if flag:
    print(1)
else:
    print(0)