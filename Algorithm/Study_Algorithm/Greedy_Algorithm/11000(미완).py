import sys
input = sys.stdin.readline
inp = int(input())
lis = []
count = 0
for _ in range(inp):
    lis.append(tuple(map(int, input().split())))

lis.sort(key=lambda x: (x[1], x[0]))
while lis:
    start = lis[0][1]
    lis.pop(0)
    i = 0
    k = len(lis)
    while True:
        if i == len(lis):
            break
        if start <= lis[i][0]:
            start = lis[i][1]
            lis.pop(i)
            i = 0
        i += 1
    count += 1
print(count)
