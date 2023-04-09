X = int(input())

line = 1
while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    a = X
    b = line - X + 1
else:
    a = line - X + 1
    b = X

print(a, '/', b, sep='')

inp = int(input())
count = 0
i = 0
mo = 0
ja = 0
while inp >= count:
    i += 1
    count += i

if (count - i) == inp:
        if i % 2 == 1:
            mo = 1 + (inp - (count - i))
            ja = i - (inp - (count - i) + 1)

        elif i % 2 == 0:
            mo = i - (inp - (count - i) + 1)
            ja = 1 + (inp - (count - i))


elif i%2 == 1:
    mo = 1 + (inp - (count - i) - 1)
    ja = i - (inp - (count - i) - 1)


elif i%2 == 0:
    mo = i - (inp - (count - i) - 1)
    ja = 1 + (inp - (count - i) - 1)

print(str(ja)+"/"+str(mo))