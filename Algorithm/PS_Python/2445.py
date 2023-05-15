inp = int(input())

for i in range(1, 2*inp):
    if i <= inp-1:
        print('*'*i + ' '*((inp*2) - 2*i) + '*'*i)
    if i == inp:
        print('*'*(inp*2))
    if i >= inp+1:
        print('*'*())
