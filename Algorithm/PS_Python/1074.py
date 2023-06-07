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
    division = divide(n, r, c) #사분면 구하기
    start += 2**(2*(n-1)) * (division-1) #n=3일 때는 1분면 마다 16(2**(2*(n-1))*(사분면-1)) 씩 차이 n=2일땐 1분면마다 4씩
    n -= 1 #분할 완료
    if r-2**n < 0:  r = r #좌표 수정 -> (7,7) -> (7-2**(n), 7-2**(n)) -> 0보다 작기 전까지 반복 -> 0보다 작은 경우는 그대로
    else: r = r-2**n
    if c-2**n < 0:  c = c #(7, 7) -> (3, 3) -> (1, 1) || (7, 5) -> (3, 1) -> (1, 1)
    else: c = c-2**n

print(start)

#(2**(2*(n-1))은 각 사분면에서의 원소의 개수
#초기 값 : 2**(n+1) -> n=3일땐 16 n=2일땐 8  => n=3에서 분할시 - 16개(2**4) n=2에서 분할시 - 4개(2**2) n=1에서 분할시 - 1개(2**0)