import sys
input = sys.stdin.readline
lis = []
cnt = 0
def queue(lis1):
    global cnt
    if lis1[0] == 'push':
        lis.append(int(lis1[1]))
    elif lis1[0] == 'pop':
        if len(lis) - cnt == 0:
            print(-1)
        else:
            print(lis[cnt])
            cnt += 1
    elif lis1[0] == 'size':
        print(len(lis)-cnt)
    elif lis1[0] == 'empty':
        if len(lis) - cnt == 0:
            print(1)
        else:
            print(0)
    elif lis1[0] == 'front':
        if len(lis) - cnt == 0:
            print(-1)
        else:
            print(lis[cnt])
    elif lis1[0] == 'back':
        if len(lis) - cnt == 0:
            print(-1)
        else:
            print(lis[-1])

inp = int(input())
for _ in range(inp):
    lis2 = input().split()
    queue(lis2)