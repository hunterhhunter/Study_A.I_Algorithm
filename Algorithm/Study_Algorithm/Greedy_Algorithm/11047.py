n, mo = map(int, input().split())
lis = []
count = 0
for _ in range(n):
    lis.append(int(input()))

for i in lis[::-1]:
    if mo // i > 0:
        count += mo // i
        mo %= i
    if mo == 0:
        break
print(count)