nums, ban = map(int, input().split())
ba = [i for i in range(1, nums+1)]

for _ in range(ban):
    a, b = map(int, input().split())
    c = ba[b-1]
    ba[b-1] = ba[a-1]
    ba[a-1] = c

for i in range(nums):
    print(ba[i], end=' ')