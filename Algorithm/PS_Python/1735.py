def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)

a, b = map(int, input().split())
c, d = map(int, input().split())

ja = a * d + b * c
mo = b * d
print(ja//GCD(ja, mo), mo//GCD(ja, mo))