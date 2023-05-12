from collections import deque
n, m = map(int, input().split())
lis = [-1] * 100001
q = deque()
q.append(n)
lis[n] = 0
while q:
    x = q.popleft()
    if x == m:
        print(lis[x])
        break
    for i in (2*x, x-1, x+1):
        if 0 <= i < 100001 and lis[i] == -1:
            if i == 2*x:
                lis[i] = lis[x]
                q.append(i)
            else:
                lis[i] = lis[x] + 1
                q.append(i)