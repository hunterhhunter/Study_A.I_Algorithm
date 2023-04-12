while True:
    lis = []
    one, two, three = 0, 0, 0
    lis.append(map(int, input().split()))
    for r in lis:
        if lis.count(r) == 1:
            one = r
        elif lis.count(r) == 2:
            two = r
        elif lis.count(r) == 3:
            three = r
    if max(lis) >
        if lis.count(three) == 3:
            print('Equilateral')
        elif lis.count(two) == 2:
            print('Isosceles')