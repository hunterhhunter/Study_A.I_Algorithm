inp = input().upper()
lis = [0 for _ in range(26)]
al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(al)):
    lis[i] = inp.count(al[i])

if lis.count(max(lis)) > 1:
    print('?')
else:
    print(al[lis.index(max(lis))])

inp = input().upper()
inp_list = list(set(inp))

cnt = []

for i in inp_list:
    count = inp.count
    cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(inp_list[(cnt.index(max(cnt)))])