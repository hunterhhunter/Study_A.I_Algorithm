import sys
input = sys.stdin.readline
inp = int(input())
stack1 = []
def stack(lis):
    global stack1
    if lis[0] == 'push':
        stack1.append(lis[1])
    elif lis[0] == 'top':
        if len(stack1) == 0:
            return -1
        else:
            return stack1[len(stack1)-1]
    elif lis[0] == 'pop':
        if len(stack1) == 0:
            return -1
        else:
            return stack1.pop()
    elif lis[0] == 'size':
        return len(stack1)
    elif lis[0] == 'empty':
        if len(stack1) == 0:
            return 1
        else:
            return 0
for _ in range(inp):
    a = input().split()
    if a[0] == 'push':
        stack(a)
    else:
        print(stack(a))