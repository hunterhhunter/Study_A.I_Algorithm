import sys
input = sys.stdin.readline
inp = int(input())
lis = list(map(int, input().split()))
dic = dict()
inp2 = int(input())
lis2 = list(map(int, input().split()))
lis3 = []
for i in lis:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for i in lis2:
    if i in dic.keys():
        lis3.append(dic[i])
    else:
        lis3.append(0)
print(*lis3)