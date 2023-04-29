# ea, bags = map(int, input().split())
# value = [list(map(int, input().split())) for _ in range(ea)]
# result = 0
# value.sort(key=lambda x: x[1], reverse=True)
# for _ in range(bags):
#     weight = int(input())
#     for i in range(len(value)):
#         if value[i][1] <= 0:
#             pass
#         else:
#             if i <= weight:
#                 result += value[i][1]
#                 value[i][1], value[i][0] = 0, 0
#                 break
# print(result)
import sys
input = sys.stdin.readline
ea, bags = map(int, input().split())
value = dict()
result = 0
for _ in range(ea):
    a, b = map(int, input().split())
    value[a] = b
value = dict(sorted(value.items(), key=lambda x: x[1], reverse=True))
for _ in range(bags):
    weight = int(input())
    for i in value.keys():
        if i <= 0:
            pass
        else:
            if i <= weight:
                result += value[i]
                value[0] = value.pop(i)
                break
print(result)

# import sys
# input = sys.stdin.readline
# ea, bags = map(int, input().split())
# value = tuple(tuple(map(int, input().split())) for _ in range(ea))
# result = 0
# value = sorted(value, key=lambda x: x[1])
# # value = dict(sorted(value.items(), key=lambda x: x[1], reverse=True))
# # for _ in range(bags):
# #     weight = int(input())
# #     for i in value.keys():
# #         if i <= 0:
# #             pass
# #         else:
# #             if i <= weight:
# #                 result += value[i]
# #                 value[0] = value.pop(i)
# #                 break
# for i in value:
#     print(*i)
