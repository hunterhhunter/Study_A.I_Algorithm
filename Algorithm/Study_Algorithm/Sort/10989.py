#계수정렬
import sys
input = sys.stdin.readline
inp = int(input())
lis = [0] * 10000

for _ in range(inp):
    lis[int(input())-1] += 1
for i in range(10000):
    if lis[i] != 0:
        for x in range(lis[i]):
            print(i+1)