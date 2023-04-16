n = int(input())
lis = sorted(map(int, input().split()))
count = 0
i = 0
result = 0
while True:
    if len(lis[i:i+lis[i]]) >= lis[i]:
        i += lis[i] + 1
        if i >= len(lis):
            i = len(lis) - 1
        count += 1
    else:
        break
print(count)

for i in lis:
    count += 1
    if count >= i:
        count = 0
        result += 1