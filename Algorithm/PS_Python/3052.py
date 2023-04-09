lis = [int(input()) for _ in range(10)]
lis1 = []

for i in range(0,10):
    lis1.append(lis[i] % 42)

lis1 = list(set(lis1))
print(len(lis1))