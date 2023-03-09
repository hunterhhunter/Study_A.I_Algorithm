# 문제 : 자연수를 입력 받은 후 그 자연수보다 작은 완전수를 리스트로 출력
inp = int(input())


def yaksu(n):
    a = []  # 완전수가 담기는 리스트
    yak = []  # 약수가 담기는 리스트
    for x in range(1, int(n ** (1 / 2)) + 1):  # 약수 구하는 방법중 1부터 n의 제곱근까지 모두 나눠서 확인하는 방식 사용(시간 복잡도 제일 낮음)
        if n % x == 0:  # 약수일 때
            yak.append(x)  # 약수 리스트에 추가
            if (
                    x ** 2) != n:  # 약수가 중복 될 때 (ex : 25 (5, 5)) 같은 수가 두 개 들어가는 것을 방지하기 위한 식 (대체 식 : n**(1/2) != x, x != (n//x))
                yak.append(n // x)  # 각 약수의 짝이되는 약수 추가
    yak.sort()  # 정렬
    yak.remove(n)  # 약수에 본인 제외(완전수를 찾기 위해)

    if sum(yak) == n:  # 완전수 일경우
        a.append(n)  # a에 추가

    return a


print([i for i in range(1, inp + 1) if yaksu(i)])  # i를 range만큼 반복하는데 조건문이 True라면 i가 들어감
# 그래서 30을 입력하면 1부터 30까지 실행해서 완전수인 수를 리스트로 만들어 출력
