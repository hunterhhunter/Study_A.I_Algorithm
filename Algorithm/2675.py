ip = int(input())

for i in range(ip):
    a, b = input().split()
    for z in b:
        print(z*int(a), end='')
    print()