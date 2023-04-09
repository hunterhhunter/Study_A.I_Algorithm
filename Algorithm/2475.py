inp = input()
inp = inp.replace(' ', '')
sum = 0
for x in inp:
    sum += int(x) ** 2
print(sum%10)