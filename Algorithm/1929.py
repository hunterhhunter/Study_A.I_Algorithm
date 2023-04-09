inp, inp2 = map(int, input().split())
for i in range(inp, inp2 + 1):
    for x in range(2, int(i**0.5) + 1):
        if i % x == 0:
            break
    else:
        if i == 1:
            pass
        else:
            print(i)