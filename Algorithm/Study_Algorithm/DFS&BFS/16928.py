from collections import deque
n, m = map(int, input().split())
pan = [0] * 101
dice = [1, 2, 3, 4, 5, 6]
sadary = []
snake = []
for _ in range(n):
    x, y = map(int, input().split())
    sadary.append((x, y))
for _ in range(m):
    x, y = map(int, input().split())
    snake.append((x, y))

sadary_start = [r[0] for r in sadary]
sadary_end = [r[1] for r in sadary]
snake_start = [r[0] for r in snake]
snake_end = [r[1] for r in snake]

q = deque()
q.append(1)

while q:
    z = q.popleft()
    if z == 100:
        break
    try:
        for i in range(6):
            move = z+dice[i]
            if pan[move] == 0:
                pan[move] = pan[z] + 1
                if move in sadary_start:
                    werp = sadary_start.index(move)
                    if pan[sadary_end[werp]] == 0:
                        pan[sadary_end[werp]] = pan[move]
                    q.append(sadary_end[werp])
                elif move in snake_start:
                    werp = snake_start.index(move)
                    if pan[snake_end[werp]] == 0:
                        pan[snake_end[werp]] = pan[move]
                    q.append(snake_end[werp])
                else:
                    q.append(move)
    except IndexError:
        pass
print(pan[100])