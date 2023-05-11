from collections import deque
max_num = 100001
su, do = map(int, input().split())
visit = [0] * max_num

def bfs():
    q = deque()
    q.append(su)
    while q:
        x = q.popleft()
        if x == do:
            print(visit[x])
            break
        for i in (x+1, x-1, x*2): #이동할 수 있는 방법이 3가지 ->
            if 1 <= i < max_num and not visit[i]:
                visit[i] = visit[x] + 1
                q.append(i)
bfs()
import sys
from collections import deque

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return array[v]
        for next_v in (v-1, v+1, 2*v):
            if 0 <= next_v < MAX and not array[next_v]:
                array[next_v] = array[v] + 1
                q.append(next_v)


MAX = 100001
n, k = map(int, sys.stdin.readline().split())
array = [0] * MAX
print(bfs(n))