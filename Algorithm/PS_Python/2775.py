inp = int(input())

for _ in range(inp):
    cn = int(input())
    ho = int(input())
    lis = [[i for i in range(1, ho+1)]]

    for x in range(cn):
        lis2 = []
        lis2.append(1)
        for z in range(1,ho):
            lis2.append(lis2[z-1]+lis[x][z])
        lis.append(lis2)

    print(lis[cn][ho-1])