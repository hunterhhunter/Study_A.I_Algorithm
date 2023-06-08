inp = int(input())

lis = []
for _ in range(inp):
    wei, lent = map(int, input().split())
    lis.append((wei, lent))

for i in lis:
    cnt = 1
    for j in lis:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    print(cnt, end=' ')

    #나보다 둘 다 큰사람 보면 +1 해서 랭크 출력하면 됨