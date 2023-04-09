n, k = map(int, input().split())
lis = []

for i in range(1, int(n**(1/2)) + 1):
    if n % i == 0:
        lis.append(i)
        if n/i not in lis:
            lis.append(int(n / i))
lis = sorted(lis)
if len(lis) < k:
    print(0)
else:
    print(lis[k-1])