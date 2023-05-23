from collections import deque

a, b = map(int, input().split())
indexes = list(map(int, input().split()))
q = deque(i for i in range(1, a+1))
re = 0

def first():
    z = q.popleft()
    if z in indexes:
        indexes.remove(z)

def second():
    z = q.popleft()
    q.append(z)

def third():
    z = q.pop()
    q.appendleft(z)

while indexes:
    ma = indexes[0]
    le = len(q)

    ap = q.index(ma)
    dei = le - q.index(ma)

    if q[0] == ma:
        first()
    elif ap >= dei:
        third()
        re += 1
    else:
        second()
        re += 1
print(re)