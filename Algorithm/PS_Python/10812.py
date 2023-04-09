nums, bun = map(int, input().split())
bucket = [_ for _ in range(1, nums+1)]

for _ in range(bun):
    begin, end, stand = map(int, input().split())
    bucket[begin-1:end] = bucket[stand-1:end] + bucket[begin-1:stand-1]

print(*bucket)