inp = int(input())
def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)
for _ in range(inp):
    a, b = map(int, input().split())
    c = GCD(a, b)
    print(c * (a//c) * (b//c))
