inp = int(input())
lis = [25, 10, 5, 1]
lis1 = []

for _ in range(inp):
    mos = int(input())
    mo = 0
    for i in lis:
        mo = mos // int(i)
        lis1.append(mo)
        mos = mos % int(i)

    print(*lis1)
    lis1 = []