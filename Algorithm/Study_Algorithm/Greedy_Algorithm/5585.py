inp = 1000 - int(input())
lis = [500, 100, 50, 10, 5, 1]
cnt = 0
for i in lis:
    if inp // i >= 1:
        cnt += inp // i
        inp %= i
print(cnt)