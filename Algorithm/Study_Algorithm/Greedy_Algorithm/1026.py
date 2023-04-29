inp = int(input())
lis1 = list(map(int, input().split()))
lis2 = list(map(int, input().split()))
result = 0
lis1.sort(reverse=True)
lis2.sort()
for i in range(inp):
    result += lis1[i] * lis2[i]
print(result)