#가장 큰 소인수 구하기
#600851475143의 가장 큰 소인수 구하기

#접근 : 소수 리스트들을 만들어 그걸 이용해 소인수들을 판별 => 큰값 출력 ----- 시간이 너무 오래걸림
#처음 코드
lis = []
for i in range(2, int(600851475143**0.5)+1):
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            break
    else:
        lis.append(i)
        if 600851475143//i in lis:
            pass
        else:
            lis.append(600851475143//i)
lis.sort()
so = []
z = 600851475143
for i in lis:
    if z % i == 0:
        so.append(i)
        z //= i

print(max(so))

#다른 사람 코드
#소인수를 모두 곱하면 결국 그 수가 나옴 => 그럼 리스트에 구한 소인수들을 저장한 후 그걸 다 곱해서 목표값이 나오면 탈출하면댐
#그리고 리스트의 마지막 수가 가장 큰 소인수가 됨 ----- 시간 개빠름
def Factorization(a):
    lst=[]
    for i in range(1,a+1):
        if a%i==0:
            lst.append(i)
            ans=1
            for n in lst:
                ans*=n
            if ans==a:
                break
    return lst[-1]
print(Factorization(600851475143))

#접근 : 소수집합을 구하지 않고 푸는 방법에 대한 생각
#소수인지 검사 and 소인수일 때 리스트에 추가?
#

#다시 보며 이해해야할 필요가 있는 코드
number = 600851475143
divisor = 2
prime_factor = [1]
result = 0

# 숫자의 소인수 구하기
while divisor < number // 2:
    if number % divisor == 0:
        prime_factor.append(divisor)
        number = number // divisor
    else:
        divisor += 1
prime_factor.append(number)

# 가장 큰 소인수 구하기
for r in prime_factor:
    if result < r:
        result = r

# 결과
print(result)