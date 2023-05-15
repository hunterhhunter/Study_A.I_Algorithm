inp = int(input())

a = input()
dic = {}
al = 'abcdefghijklmnopqrstuvwxyz'
z = 1
result = 0
for i in al:
    dic[i] = z
    z += 1
i = 0
for x in a:
    result += dic[x]*(31**i)
    i += 1
print(result%1234567891)