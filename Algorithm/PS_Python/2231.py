inp = int(input())
lis = []

for x in range(1, inp + 1):
    make = x
    a = x
    for i in range(6, -1, -1):
        make += a // (10**i)
        a = a % (10 ** i)

    if make == inp:
        lis.append(x)

if len(lis) == 0:
    print(0)
else:
    print(min(lis))