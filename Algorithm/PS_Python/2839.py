# inp = int(input())
# lis = []
# x = 1
# y = 1
# z = 7
# while z < inp-1:
#     z += 1
#     if x >= 3:
#         x -= 3
#         y += 2
#     else:
#         y -= 1
#         x += 2
# if inp < 8:
#     if inp % 3 == 0:
#         print(inp//3)
#     elif inp % 5 == 0:
#         print(inp//5)
#     else:
#         print(-1)
#
# else:
#     print(x+y)

inp = int(input())
count = 0
while inp >= 0:
    if inp % 5 == 0:
        count += inp//5
        print(count)
        break
    inp -= 3
    count += 1
else:
    print(-1)
