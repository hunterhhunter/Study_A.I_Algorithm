import sys
import heapq
input = sys.stdin.readline
inp = int(input())
lis = []
count = 0
for _ in range(inp):
    start, end = map(int, input().split())
    lis.append([start, end])

lis.sort()

room = []
heapq.heappush(room, lis[0][1])

for i in range(1, inp):
    if lis[i][0] < room[0]:
        heapq.heappush(room, lis[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, lis[i][1])
print(len(room))



# while lis:
#     start = lis[0][1]
#     lis.pop(0)
#     i = 0
#     k = len(lis)
#     while True:
#         if i == len(lis):
#             break
#         if start <= lis[i][0]:
#             start = lis[i][1]
#             lis.pop(i)
#             i = 0
#         i += 1
#     count += 1
#
