inp = input()

lis = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in lis:
    inp = inp.replace(i, '*')

print(len(inp))