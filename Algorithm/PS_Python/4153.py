while True:
    lis = list(map(int, input().split()))
    ma = max(lis)
    lis.remove(max(lis))
    if lis[0] == 0 or lis[1] == 0:
        break
    if (lis[0]**2) + (lis[1]**2) == (ma**2):
        print("right")
    else:
        print("wrong")