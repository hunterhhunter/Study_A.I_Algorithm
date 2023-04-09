inp = int(input())
inp2 = int(input())
lis2 = []
for i in range(inp, inp2 + 1):
    for x in range(2, int(i**0.5) + 1):
        if i % x == 0:
            break
    else:
        if i == 1:
            pass
        else:
            lis2.append(i)
if not lis2:
    print(-1)
else:
    print(sum(lis2))
    print(lis2[0])