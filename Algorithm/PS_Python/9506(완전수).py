a = 0
while True:
    a = int(input())
    if a == -1:
        break
    lis = []
    for i in range(1, int(a**(1/2)) + 1): #약수를 구하는 다양한 방법 중 한 가지 -> 연산 횟수를 최대한 줄여봄
        if a % i == 0: # 입력값이 나누어 떨어질 때
            lis.append(i) # 약수인 것이니 리스트에 넣어주기
            if a/i not in lis: # 나누어 떨어졌을 때 얻을 수 있는 정보 -> 약수로 원래 수를 나눴을 때 나오는 수 또한 약수다.
                lis.append(int(a / i)) # 그래서 리스트에 넣어주는데 리스트에 없을 때만
    lis = sorted(lis) # 정렬하기
    lis.remove(a) #자기 자신 제거

    if sum(lis) == a: #완전수인가? sum함수를 사용
        print(f"{a} = ", end='') #출력 형식에 맞춰 출력한다.
        for i in range(len(lis)-1):
            print(f"{lis[i]} + ", end='')
        print(lis[-1])
    else:
        print(f"{a} is NOT perfect.")