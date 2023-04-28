a, b = map(int, input().split())

lis = set(map(int, input().split()))
lis2 = set(map(int, input().split()))

lis3 = list(lis ^ lis2)
print(len(lis3))