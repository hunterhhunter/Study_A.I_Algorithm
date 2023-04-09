su, bun = map(int, input().split())
bucket = [_ for _ in range(1, su+1)]

for i in range(bun):
    a, b = map(int, input().split())

    reverse_bucket = bucket[a-1:b][::-1]
    bucket[a-1:b] = reverse_bucket

print(*bucket)