a = [1, 2, 3, 4, 5, 6, 7, 8]
b = list(reversed(a))
com = list(map(int, input().split()))

if com == a:
    print("ascending")
elif com == b:
    print("descending")
else:
    print('mixed')