su, goal = map(int, input().split())
lis = list(map(int, input().split()))
a = []
for i in range(len(lis)):
    if lis[i] < goal:
        print(lis[i], end=' ')
