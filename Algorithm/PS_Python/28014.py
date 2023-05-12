inp = int(input())
lis = list(map(int, input().split()))
cnt = 1
for i in range(1, inp):
    if lis[i-1] > lis[i]:
        continue
    else:
        cnt += 1
print(cnt)
