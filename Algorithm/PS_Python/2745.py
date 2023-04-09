N, B = input().split()
N = N[::-1]
B = int(B)

table = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

res = 0

for i in range(len(N)):
    res += table.index(N[i]) * (B ** i)

print(res)

# n, b = map(str, input().split())
# b = int(b)
# count = 1
# su = 0
# st = list(range(10))
# st = str(st)
#
# for i in range(len(n)):
#     if b > 10:
#         if n[i] in st:
#             su += int(n[i]) * (b ** (len(n)-count))
#             count += 1
#         else:
#             su += (ord(n[i])-55) * (b ** (len(n)-count))
#             count += 1
#     else:
#         su += int(n[i]) * (b ** (len(n)-count))
#         count += 1
# print(su)