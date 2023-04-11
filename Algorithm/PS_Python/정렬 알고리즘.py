inp = int(input())
li = []
for _ in range(inp):
    li.append(int(input()))

def bubble(lis):
    for i in range(len(lis)):
        for x in range(i, len(lis)):
            if lis[i] > lis[x]:
                tmp = lis[x]
                lis[x] = lis[i]
                lis[i] = tmp
    print(*lis)

def select(lis):
    for i in range(len(lis)):
        mi = i
        for x in range(i+1, len(lis)):
            if lis[x] < lis[mi]:
                mi = x
        lis[i], lis[mi] = lis[mi], lis[i]
    print(*lis)



select(li)