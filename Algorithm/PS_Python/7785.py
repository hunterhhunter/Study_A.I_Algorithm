inp = int(input())
lis = dict()
for _ in range(inp):
    name, log = input().split()
    if log == 'enter':
        lis[name] = True
    else:
        lis[name] = False
lis1 = []
for name, log in lis.items():
    if log:
        lis1.append(name)
    else:
        pass
lis1.sort(reverse=True)
for i in lis1:
    print(i)