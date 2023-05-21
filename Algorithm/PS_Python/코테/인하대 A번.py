inp = input()
lis = ['M', 'O', 'B', 'I', 'S']
re = 0
for i in lis:
    if inp.count(i) > 0:
        re += 1

if re > 4:
    print('YES')
else:
    print('NO')