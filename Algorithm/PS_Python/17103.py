import sys
input = sys.stdin.readline
inp = int(input().rstrip())
lis = [True for _ in range(1000001)]
lis[0], lis[1] = False, False
for i in range(2, 1000):
    if lis[i]:
        for j in range(i+i, 1000001, i):
            lis[j] = False

for _ in range(inp):
    cnt = 0
    inp2 = int(input().rstrip())
    for i in range(2, inp2//2+1):
        if lis[i] and lis[inp2-i]:
            cnt += 1
    print(cnt)
