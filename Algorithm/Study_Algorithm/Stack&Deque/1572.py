import sys
input = sys.stdin.readline

n, k = map(int, input().split())

from collections import deque
from bisect import bisect_left
lis = [int(input()) for _ in range(n)]

su = 0

st = lis[:k]
ed = lis[k:]
q = deque(st)
st.sort()
mid = (k-1)//2 # (k+2)//2 -1
su += st[mid]

for i in range(k, n):
    ls = lis[i-k:i]
    le = sorted(ls)
    su += le[mid]

print(su)