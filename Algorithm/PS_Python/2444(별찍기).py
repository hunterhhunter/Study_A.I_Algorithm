#첫 번째 코드
#정석적인 문제풀이 -> for 구문을 2번 사용해
#처음 4줄 출력 후 아래 5줄 출력
inp = int(input())
for i in range(1, inp):
    print(' ' *(inp-i) + '*'*(2*i - 1))
for x in range(inp, 0, -1):
    print(' '*(inp-x) + '*'*(2*x-1))

# 두 번째 코드
# 난 for 구문 한 번만 쓸래 -> 객기에서 나온 이상한 코드
# 조건문의 반환값이 True, False인 것을 이용한 문자열 연산
inp = int(input())
for n in range(1, 2*inp):
    big = int((n <= inp))
    small = int((n > inp))
    print(' ' * (inp-n) * big + '*'*(2*n - 1) * big + small * ' '*(n % inp)
          + small * '*'*((2 * inp-1) - (n % inp)*2))
    #굳이 굳이 한 번에 더했음 ㅋㅋ

#세 번째 코드
# 줄이고자 객기부린 코드
for n in range(1, 2 * inp):
    spaces = ' ' * abs(inp - n) #절댓값을 이용해 공백의 개수를 줄였다 늘림
    stars = '*' * (2 * min(n, 2 * inp - n) - 1) # min 함수를 이용해 점점 n값이 증가하면서 별 개수 선정
    print(spaces + stars)

# ...?
# 그냥 하지마
np = int(input())
[print(' ' * abs(inp - n) + '*' * (2 * min(n, 2 * inp - n) - 1)) for n in range(1 , 2 * inp)]