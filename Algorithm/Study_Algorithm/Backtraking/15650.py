n, m = map(int, input().split())
s = []
def dfs():
    if len(s) == m:
        for i in s:
            print(*i)
        return