a, b = map(int, input().split())
lis = list(map(int, input().split()))
lis.sort(reverse=True)
print(lis[b-1])