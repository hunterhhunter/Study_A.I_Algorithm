inp = int(input())

for _ in range(inp):
    cng, bang, num = map(int, input().split())
    if cng == 1:
        c_cng = '1'
        c_ho = num // cng
    else:
        if num % cng == 0:
            c_cng = str(cng)
            c_ho = num // cng
        else:
            c_cng = str(num % cng)
            c_ho = num//cng + 1
    if c_ho >= 10:
        c_ho = str(c_ho)
    else:
        c_ho = '0' + str(c_ho)

    print(c_cng + c_ho)

inp = int(input())
for _ in range(inp):
    cng, bang, num = map(int, input().split())
    floor = num % cng
    loomline = (num//cng) + 1
    if floor == 0:
        floor = cng
        loomline -= 1
    print(floor*100 + loomline)
