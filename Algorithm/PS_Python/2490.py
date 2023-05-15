for _ in range(3):
    lis = list(map(int, input().split()))

    d = lis.count(0)

    if d == 0:
        print('E')
    elif d == 1:
        print('A')
    elif d == 2:
        print('B')
    elif d == 3:
        print('C')
    else:
        print('D')