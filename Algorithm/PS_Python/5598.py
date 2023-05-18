inp = input()

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
kaisar = 'DEFGHIJKLMNOPQRSTUVWXYZABC'
re = ''
for i in inp:
    re += alpha[kaisar.index(i)]
print(re)