n, m = map(int, input().split())
lis = list(map(int, input().split()))
ma = 0
for i in range(len(lis)):
    for x in range(i+1, len(lis)):
        for z in range(x+1, len(lis)):
            if lis[i] + lis[x] + lis[z] > m:
                continue
            else:
                ma = max(lis[i] + lis[x] + lis[z], ma)
print(ma)