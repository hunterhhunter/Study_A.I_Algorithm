from collections import deque
import sys
input = sys.stdin.readline
inp = int(input())
deck = deque()

def Que(lis):
    move = lis[0]
    if move == 'push_back':
        deck.append(lis[1])
    elif move == 'push_front':
        deck.appendleft(lis[1])
    elif move == 'pop_front':
        if len(deck) == 0:
            return -1
        else:
            return deck.popleft()
    elif move == 'pop_back':
        if len(deck) == 0:
            return -1
        else:
            return deck.pop()
    elif move == 'size':
        return len(deck)
    elif move == 'empty':
        if len(deck) == 0:
            return 1
        else:
            return 0
    elif move == 'front':
        if len(deck) == 0:
            return -1
        else:
            return deck[0]
    elif move == 'back':
        if len(deck) == 0:
            return -1
        else:
            return deck[-1]

for _ in range(inp):
    lis = list(input().split())
    if lis[0][0:4] == 'push':
        Que(lis)
    else:
        print(Que(lis))