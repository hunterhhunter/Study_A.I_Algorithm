inp = int(input())

for _ in range(inp):
    in2 = int(input())
    while True:
        for x in range(2, int(in2**0.5) + 1):
            if in2 % x == 0:
                in2 += 1
                break
        else:
            if in2 == 1 or in2 == 0:
                print(2)
                break
            else:
                print(in2)
                break