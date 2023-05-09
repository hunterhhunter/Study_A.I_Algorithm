inp = int(input())
lis = [int(input()) for _ in range(inp)]
dic = dict()
for i in lis:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
lis2 = sorted(lis)
print(round(sum(lis)/len(lis)))
print(lis2[len(lis)//2])
print(max(dic.values()))
print(lis2[-1] - lis2[0])
