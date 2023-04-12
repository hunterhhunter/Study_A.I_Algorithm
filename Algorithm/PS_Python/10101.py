lis = [int(input()) for _ in range(3)]
z = 0
for r in lis:
    if lis.count(r) == 2:
        z = r

if sum(lis) == 180:
    if lis.count(60) == 3:
        print('Equilateral')
    elif lis.count(z) == 2:
        print('Isosceles')
    elif sum(lis) == 180:
        print('Scalene')
else:
    print('Error')