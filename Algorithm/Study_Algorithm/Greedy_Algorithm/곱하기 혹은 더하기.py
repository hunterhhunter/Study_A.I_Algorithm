inp = input()
ma = 0
for i in inp:
    num = int(i)
    if num <= 1 or ma <= 0:
        ma += num
    else:
        ma *= num
print(ma)
