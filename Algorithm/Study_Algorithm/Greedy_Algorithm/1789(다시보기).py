inp = int(input())
n = 1
result = 0

while n*(n+1)/2 <= inp:
    n += 1
print(n-1)