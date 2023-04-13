import math
m = 123456
lis = [True for _ in range(2 * m + 1)]
lis[0], lis[1] = False, False

for i in range(2, int(math.sqrt(m * 2)) + 1):
    if lis[i]:
        j = 2
        while i * j <= 2 * m:
            lis[i * j] = False
            j += 1

while True:
    inp = int(input())
    if inp == 0:
        break

    count = 0

    for i in range(inp+1, 2*inp+1):
        if lis[i]:
            count += 1
    print(count)