a, b = map(int, input().split())
lis = [0]
for i in range(1, b+1):
    for j in range(i):
        lis.append(i)

print(sum(lis[a:b+1]))
