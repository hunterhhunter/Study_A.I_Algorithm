inp = int(input())
dic = {'A':0, 'B':0, 'C':0}
lis = [300, 60, 10]
if inp % 10 != 0:
    print(-1)
else:
    x = 0
    for i in dic.keys():
        dic[i] += inp//lis[x]
        inp %= lis[x]
        x += 1
    for i in dic.values():
        print(i, end=' ')