gwa = int(input())
lis = list(map(int, input().split()))

cho = max(lis)
chong = sum(lis)
pyung = (chong / gwa) / cho * 100

print(pyung)
