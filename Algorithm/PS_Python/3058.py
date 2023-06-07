inp = int(input())

for _ in range(inp):
    lis = list(map(int, input().split()))
    su = 0
    ma = max(lis)
    for i in lis:
        if i % 2 == 0:
            su += i
            if ma > i:
                ma = i
    print(su, ma)