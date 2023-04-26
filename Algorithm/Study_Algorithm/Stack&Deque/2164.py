import sys
from collections import deque
input = sys.stdin.readline
inp = int(input())

lis = deque(r for r in range(1, inp + 1))
def remov():
    lis.popleft()
def po():
    lis.append(lis.popleft())

while len(lis) > 1:
    remov()
    po()
print(*lis)