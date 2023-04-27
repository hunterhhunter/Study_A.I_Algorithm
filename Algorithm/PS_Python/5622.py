inp = list(input())
alpha = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

for i in alpha:
    for x in i:
        for z in inp:
            if x == z:
                time += alpha.index(i) + 3

print(time)
