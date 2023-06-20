a, b = map(int, input().split()) #공백을 기준으로 입력받는 방법

if 100*a >= b: #조건분기 -> 100원짜리 동전이기 때문 -> 총 금액 알아내기
    print('Yes') # 출력
else: # 아니다?
    print('No') #출력