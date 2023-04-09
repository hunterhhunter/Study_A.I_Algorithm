ip = input()
lis = 'abcdefghijklmnopqrstuvwxyz'

for i in lis:
    if i in ip:
        print(ip.index(i),end=' ')
    else:
        print(-1, end=' ')