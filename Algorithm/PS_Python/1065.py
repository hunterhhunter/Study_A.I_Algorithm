inp = int(input())
cnt = 99
if inp < 100:
    print(inp)
else:
    for i in range(100, inp+1):
        lis = list()
        absol = []
        for x in str(i):
            lis.append(int(x))
        for z in range(1, len(lis)):
            absol.append(lis[z] - lis[z-1])
        for d in range(1, len(absol)):
            if absol[d] != absol[d-1]:
                break
        else:
            cnt += 1
    print(cnt)