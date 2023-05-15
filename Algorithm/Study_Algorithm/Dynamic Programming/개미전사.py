inp = int(input())

lis = list(map(int, input().split()))

d = [0] * 100
d[0] = lis[0]
d[1] = max(lis[0], lis[1])
for i in range(2, inp):
    d[i] = max(d[i-1], d[i-2]+lis[i])
print(d[inp - 1])