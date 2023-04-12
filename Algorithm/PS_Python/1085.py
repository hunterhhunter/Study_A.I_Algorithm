x, y, w, h = map(int, input().split())

lis = [x, y, w-x, h-y]
print(min(lis))