a, b = map(int, input().split())
lis1 = list(map(int, input().split()))
lis2 = list(map(int, input().split()))
lis1.sort()
lis2.sort(reverse=True)

for i in range(b):
    if lis1[i] < lis2[i]:
        lis1[i], lis2[i] = lis2[i], lis1[i]
    else:
        break
print(sum(lis1))
