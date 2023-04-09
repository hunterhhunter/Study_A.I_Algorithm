inp = int(input())
for i in range(1, inp):
    print(' ' *(inp-i) + '*'*(2*i - 1))
for x in range(inp, 0, -1):
    print(' '*(inp-x) + '*'*(2*x-1))