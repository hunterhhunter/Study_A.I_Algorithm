#1부터 n까지 순회할거임
# 그 수를 제외하고 수를 고름 -> m번

n, m = map(int, input().split())
s = []
visit = [False] * (n+1)

def dfs():
    if len(s) == m:
        print(*s)
        return
    for i in range(1, n+1):
        if visit[i]:
            continue
        visit[i] = True
        s.append(i)
        dfs()
        s.pop()
        visit[i] = False
dfs()

def dfs2():
    if len(s) == m:
        print(*s)
        return
    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs2()
            s.pop()
dfs2()
