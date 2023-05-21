inp = int(input())

lemon = list(map(int, input().split()))

for i in range(len(lemon)):
    if i == inp-1:
        lemon[i] = lemon[i] - 1
    else:
        lemon[i] = lemon[i] - len(lemon[i + 1:inp])
print(max(lemon))
