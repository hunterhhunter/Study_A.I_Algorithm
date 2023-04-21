lis = []
for _ in range(5):
    lis.append(int(input()))
print(sum(lis)//len(lis))
lis.sort()
print(lis[2])