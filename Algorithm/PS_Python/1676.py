n = int(input())
a = 1
for i in range(2, n+1):
    a *= i
a = str(a)
cnt = 0
a = a[::-1]
for i in a:
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)
