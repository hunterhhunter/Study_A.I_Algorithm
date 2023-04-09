lis = [int(input()) for _ in range(28)]
lis2 = [i for i in range(1, 31)]

lis3 = []
for i in lis2:
    if i not in lis:
        lis3.append(i)

print(*lis3)

# lis2 = [i for i in range(1, 31)]
#
# for _ in range(28):
#     applie = int(input())
#     lis2.remove(applie)
#
# print(*lis2)