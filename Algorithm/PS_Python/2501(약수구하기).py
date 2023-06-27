n, k = map(int, input().split())
lis = []

for i in range(1, int(n**(1/2)) + 1): #약수를 구하는 다양한 방법 중 한 가지 -> 연산 횟수를 최대한 줄여봄
    if n % i == 0: # 입력값이 나누어 떨어질 때
        lis.append(i) # 약수인 것이니 리스트에 넣어주기
        if n//i not in lis: # 나누어 떨어졌을 때 얻을 수 있는 정보 -> 약수로 원래 수를 나눴을 때 나오는 수 또한 약수다.
            lis.append(n // i) # 그래서 리스트에 넣어주는데 리스트에 없을 때만
lis = sorted(lis) #정렬하기
if len(lis) < k: # 약수의 개수가 원하는 순서의 수보다 작을 때는 출력이 불가하므로 0 출력
    print(0)
else: #출력이 가능하다면 k번째 수가 아닌 k - 1번째 수 -> 인덱스는 0번부터 시작한다.
    print(lis[k-1])