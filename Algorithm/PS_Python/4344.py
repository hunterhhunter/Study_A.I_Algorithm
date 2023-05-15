inp = int(input())

for _ in range(inp):
    lis = list(map(int, input().split()))
    n = lis.pop(0)
    cnt = 0
    avg = sum(lis) / n
    for i in lis:
        if i > avg:
            cnt += 1
    rate = round((cnt / n) * 100)

    print(f"{rate:.3f}%")