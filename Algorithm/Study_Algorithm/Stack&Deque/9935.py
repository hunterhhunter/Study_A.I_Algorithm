inp = input()
c4 = input()
ans = []
z = 0
for i in inp:
    ans.append(i)
    z += 1
    if len(ans) >= 1:
        if str(''.join(ans[(z-len(c4)):z])) == c4:
            for _ in range(len(c4)):
                ans.pop()
                z -= 1
if ans:
    print(''.join(ans))
else:
    print('FRULA')
