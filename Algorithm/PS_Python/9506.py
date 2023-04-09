a = 0
while True:
    a = int(input())
    if a == -1:
        break
    lis = []
    for i in range(1, int(a**(1/2)) + 1):
        if a % i == 0:
            lis.append(i)
            if a/i not in lis:
                lis.append(int(a / i))
    lis = sorted(lis)
    lis.remove(a)

    if sum(lis) == a:
        print(f"{a} = ", end='')
        for i in range(len(lis)-1):
            print(f"{lis[i]} + ", end = '')
        print(lis[-1])
    else:
        print(f"{a} is NOT perfect.")