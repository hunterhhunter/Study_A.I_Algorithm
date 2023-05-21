n, k = map(int, input().split())

star = [0] *(n+1)
visit = [False]*(n+1)

from collections import deque
q = deque()
q.append(0)
while q:
    z = q.popleft()
    try:
        visit[z] = True
        fir = z+1

        if fir <= n:
            q.append(fir)
            star[fir] = star[z] + 1
            if fir == n:
                break

    except IndexError:
        pass

q.append(0)
while q:
    z = q.popleft()
    try:
        sec = z + int((z/2))
        if sec <= n:
            q.append(sec)
            star[sec] = star[z] + 1
            if sec == n:
                break
    except IndexError:
        pass

if star[n] == k:
    print('minigimbob')
else:
    print('water')