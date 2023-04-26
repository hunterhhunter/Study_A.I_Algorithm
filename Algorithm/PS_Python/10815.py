inp1 = int(input())
lis1 = set(map(int, input().split()))
inp2 = int(input())
lis2 = list(map(int, input().split()))
lis3 = []

for x in lis2:
    if x in lis1:
        lis3.append(1)
    else:
        lis3.append(0)
print(*lis3)