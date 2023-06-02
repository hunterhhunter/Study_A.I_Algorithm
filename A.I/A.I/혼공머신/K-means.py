#K-means 작동 방식
# 1. 무작위로 k개의 클러스터 중심을 정한다.
# 2. 각 샘플에서 가장 가까운 클러스터 중심을 찾아 해당 클러스터의 샘플로 지정
# 3. 클러스터에 속한 샘플의 평균값으로 클러스터 중심을 변경한다.
# 4. 클러스터 중심에 변화가 없을 때까지 2번으로 돌아가 반복한다.

import numpy as np
fruits = np.load('fruits_300.npy')
fruits_2d = fruits.reshape(-1, 100*100)

from sklearn.cluster import KMeans
km = KMeans(n_clusters=3, random_state=42)
km.fit(fruits_2d)
#각 샘플이 어떤 레이블에 속하는지 확인하는 메서드 => 각 과일분류 결과 확인
print(km.labels_)

print(np.unique(km.labels_, return_counts=True))

#각 이미지를 출력하기 위한 draw_fruits 함수 정의

import matplotlib.pyplot as plt
def draw_fruits(arr, ratio=1):
    n = len(arr) #샘플 개수
    #한 줄에 10개씩 이미지를 그린다. 샘플 개수를 10으로 나누어 전체 행 개수를 계산한다.
    rows = int(np.ceil(n/10))
    #행이 1개면 열의 개수는 샘플 개수이다. 그렇지 않으면 10개이다. -> 행이 2개 이상이면 데이터가 10개 이상이므로 공간이 비더라도 10열로
    cols = n if rows<2 else 10
    fig, axs = plt.subplots(rows, cols, figsize=(cols*ratio, rows*ratio), squeeze=False)

    for i in range(rows):
        for j in range(cols):
            if i*10+j < n: #n개 까지만 그린다. -> 97일 경우 97까지만 그리기 위함
                axs[i, j].imshow(arr[i*10+j], cmap='gray_r')
            axs[i, j].axis('off')
    plt.show()

draw_fruits(fruits[km.labels_==0])

draw_fruits(fruits[km.labels_==1])

draw_fruits(fruits[km.labels_==2])

#클러스터의 중심 이 배열은 fruits_2d 샘플의 클러스터 중심이기에 각 중심을 이미지로 출력하려면 100*100 크기의 2차원 배열로 바꿔야 한다.
#반환값은 (클러스터의 개수, 데이터의 특징(feature))
draw_fruits(km.cluster_centers_.reshape(-1, 100, 100), ratio=3)

#KMeans 클래스는 훈련 데이터 샘플에서 클러스터 중심까지 거리로 변환해주는 transform메서드가 있다.
# -> StandardScaler 클래스처럼 특성값을 변환하는 도구로 사용할 수 있다.
# transform 메서드는 2차원 배열 입력값을 기대한다.
# fruits_2d[100]처럼 쓰면 (10000, ) 배열이 되어 에러 발생 -> fruits_2d[100:101]로 배열 전달
print(km.transform(fruits_2d[100:101]))

print(km.predict(fruits_2d[100:101]))

draw_fruits(fruits[100:101])

#KMeans는 클러스터 중심을 반복적으로 옮기며 최적의 클러스터를 찾기 때문에 알고리즘 반복 횟수는 n_iter_ 속성에 저장된다.
print(km.n_iter_)

#단점은 클러스터의 개수를 직접 지정해야함 -> 적절한 K값 찾기
#완벽한 방법은 없다 -> 저마다의 장단점을 가진 바업들 -> 대표적인 엘보우(elbow) 방식
# 클러스터와 클러스터에 속한 샘플과의 거리의 제곱 합을 이너셔(inertia) -> 각 샘플들이 얼마나 가깝게 모여있는지
# 클러스터 개수가 증가 -> 클러스터 개개의 크기가 감소 -> 이너셔 감소 => 그럼 클러스터 개수와 이너셔의 상관관계 파악 = 엘보우(elbow)방식
# 꺽이는 지점이 존재

inertia = []
for k in range(2, 7):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(fruits_2d)
    inertia.append(km.inertia_)
plt.plot(range(2, 7), inertia)
plt.xlabel('k')
plt.ylabel('inertia')
plt.show()
