#첫 번째 숫자가 두 번째 숫자의 약수, 배수 인지 구하는 것
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if b % a == 0: #나누어 떨어진다면 약수
        print("factor")
    elif a % b == 0: #나누어 떨어진다면 배수
        print("multiple")
    else:
        print("neither")