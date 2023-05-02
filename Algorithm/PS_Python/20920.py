import sys
input = sys.stdin.readline
a, b = map(int, input().rstrip().split())
dic = {}
for _ in range(a):
    inp = input().rstrip()
    if len(inp) < b:
        continue
    else:
        if inp in dic:
            dic[inp] += 1
        else:
            dic[inp] = 1

d1 = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in d1:
   print(i[0])