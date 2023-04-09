inp = int(input())
count = inp
lis = map(int, input().split())
for x in lis:
    if x == 1:
        count -= 1
    for i in range(2, x):
        if x % i == 0:
            count -= 1
            break
print(count)