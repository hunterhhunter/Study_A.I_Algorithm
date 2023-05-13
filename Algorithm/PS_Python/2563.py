inp = int(input())
lis = [[0] * 100 for _ in range(100)] #=> 문제 핵심

for _ in range(inp):
    x, y = map(int, input().split())

    for ga in range(x, x+10):
        for se in range(y, y+10):
            lis[ga][se] = 1

result = 0
for i in range(100):
    result += lis[i].count(1)

print(result)