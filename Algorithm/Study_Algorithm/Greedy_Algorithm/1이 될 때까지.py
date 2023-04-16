N, M = map(int, input().split())
count = 0
#
# while N > 1:
#     if N % M == 0:
#         N = N // M
#     else:
#         N -= 1
#     count += 1
# print(count)

while True:
    target = (N // M) * M
    count += (N - target)
    N = target
    if N < M:
        break
    count += 1
    N //= M

count += (N - 1)
print(count)