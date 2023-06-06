n, r, c = map(int, input().split())

#2 * 2 가 나올때 까지 계속 분할할 것 이 때 시작하는 시작 값은 2**(n+1)*(사분면-1) 좌표 : r,c -> r-2**n, c-2**n

def divide(n, x, y):
    mid = 2**n // 2 - 1

    if x<= mid and y <= mid:
        return 1
    elif x <= mid and y > mid:
        return 2
    elif x > mid and y <= mid:
        return 3
    elif x > mid and y > mid:
        return 4
start = 0
while n > 0:
    division = divide(n, r, c)
    start += 2**(2*(n-1)) * (division-1)
    n -= 1
    if r-2**n < 0:  r = r
    else: r = r-2**n
    if c-2**n < 0:  c = c
    else: c = c-2**n

print(start)

