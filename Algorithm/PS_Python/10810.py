nums, ban = map(int, input().split())
ba = [0 for _ in range(nums)]

for _ in range(ban):
    si, ggt, nb = map(int, input().split())
    for i in range(si-1, ggt):
        ba[i] = nb

for i in range(len(ba)):
    print(ba[i], end=' ')