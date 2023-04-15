inp = int(input())
first = 666
while inp != 0:
    if '666' in str(first):
        inp = inp-1
        if inp == 0:
            break
    first += 1
print(first)