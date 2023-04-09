N, B = map(str, input().split())
B = int(B)
res = ''
lis = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while N != 0:
    res += lis[int(N) % B]
    N = int(N) // B

print(res[::-1])