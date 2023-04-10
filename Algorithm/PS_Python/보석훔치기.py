# 입력의 첫 번째 줄에는 보석 종류의 수와 훔칠 수 있는 최대의 무게가 주어집니다.
#
# 두 번째 줄부터는 보석의 가치, 무게, 개수가 주어질 때 보석을 훔칠 수 있는 최대 가치를 구해봅시다.
#
# 단, 모든 보석은 쪼갤 수 있으며 쪼갠 만큼 가치도 줄어듭니다.

# 값을 구하는 함수입니다. 매개변수들을 이용해 지시사항을 해결해 보세요.

def countJewelry(n, weight, jewelry, value):
    # 정답을 저장할 변수입니다.
    ans = 0
    lis = list(r[0] for r in value)
    ma = max(lis)
    ans += ma * value[lis.index(ma)][1]
    now = value[lis.index(ma)][1]

    if now > weight:
        ans -= (now - weight) * ma
    elif now == weight:
        pass
    else:
        while now < weight:
            lis[lis.index(ma)] = 0
            ma = max(lis)
            if value[lis.index(ma)][1] >= weight - now:
                ans += ma * (weight - now)
                now += (weight - now)
            else:
                ans += ma * value[lis.index(ma)][1]
                now += value[lis.index(ma)][1]
    # 정답을 출력합니다.
    print(int(ans))


# 값을 입력 받는 코드입니다. 수정하지 마세요!
# 하나의 보석에 대한 정보를 리스트 형태로 저장합니다.
jewelry = []
value = []

# 보석 종류의 수와 무게를 입력 받습니다.
n, weight = list(map(int, input().split()))
# 하나의 보석에 대해 가치, 무게, 보석의 수를 리스트 형태로 입력 받습니다.
for i in range(n):
    jewelry.append(list(map(int, input().split())))
    value.append([jewelry[i][0] / jewelry[i][1], jewelry[i][2] * jewelry[i][1]])

print(*jewelry)
print(*value)

countJewelry(n, weight, jewelry, value)


def countJewelry(n, weight, jewelry):
    result = 0
    jewelry = [[a / b, b * c] for a, b, c in jewelry]

    jewelry.sort(reverse=True)

    for i in range(n):
        if weight >= jewelry[i][1]:
            result += jewelry[i][0] * jewelry[i][1]
            weight -= jewelry[i][1]
        else:
            result += jewelry[i][0] * weight
            break

    print(int(result))


n, weight = map(int, input().split())
jewelry = [list(map(int, input().split())) for i in range(n)]

countJewelry(n, weight, jewelry)