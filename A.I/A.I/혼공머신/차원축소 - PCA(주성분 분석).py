#차원축소 -> 10000개의 특성을 가진 데이터를 n개로 줄일 수 있음 -> 난 50개의 주성분을 가진 데이터로 차원을 축소하고 싶어
# 어떻게? -> 10000개의 특성 = 10000개의 축과 같은 뜻 -> 그럼 어떻게?
# 10000개의 축을 가진 300개의 데이터를 좌표상에 놓는다고 가정 -> 이 데이터들을 하나의 선에 투영하여 하나의 축 위에 모두 표시할 것
# -> 이 때 분산이 가장 큰 것 -> 가장 데이터가 넓게 분포되어있는 축을 찾기 -> 이 축이 다른 데이터 셋의 축이 됨
# -> 그럼 (300, 10000)을 가장 잘 표현하는 (300, 50)의 데이터가 생성됨

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


import numpy as np
fruits = np.load('fruits_300.npy')
fruits_2d = fruits.reshape(-1, 100*100)

from sklearn.decomposition import PCA
pca = PCA(n_components=50)
pca.fit(fruits_2d)

print(pca.components_.shape)

draw_fruits(pca.components_.reshape(-1, 100, 100))

print(fruits_2d.shape)

fruits_pca = pca.transform(fruits_2d)
print(fruits_pca.shape)

# 차원축소한 데이터를 다시 재구성하는 메서드가 존재

fruits_inverse = pca.inverse_transform(fruits_pca)
print(fruits_inverse.shape)

fruits_reconstruct = fruits_inverse.reshape(-1, 100, 100)
for start in [0, 100, 200]:
    draw_fruits(fruits_reconstruct[start:start+100])
    print()

# 주성분이 원본 데이터의 분산을 얼마나 잘 나타내는지 기록한 값 = 설명된 분산 메서드가 존재
# 처음의 분산부터 크기가 작아지며 존재 -> 분산 비율을 모두 더하면 50개의 주성분으로 표현하고있는 총 분산 비율

print(np.sum(pca.explained_variance_ratio_))

plt.plot(pca.explained_variance_ratio_)
plt.show()

#다른 알고리즘과 함께 사용하기

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

#타깃값 정해주기 (사과 0, 파인애플 1, 바나나 2)
target = np.array([0]*100 + [1]*100 + [2]*100)
#축소 안 한 2d 데이터 이용했을 때
from sklearn.model_selection import cross_validate
scores = cross_validate(lr, fruits_2d, target)
print(np.mean(scores['test_score']))
print(np.mean(scores['fit_time']))

#축소한 데이터 이용했을 때
scores = cross_validate(lr, fruits_pca, target)
print(np.mean(scores['test_score']))
print(np.mean(scores['fit_time']))

#주성분의 개수를 정해주는 것이 아닌 목표 분산을  정해줄 수도 있음
pca = PCA(n_components=0.5)
pca.fit(fruits_2d)

print(pca.n_components_)

fruits_pca = pca.transform(fruits_2d)
print(fruits_pca.shape)

scores = cross_validate(lr, fruits_pca, target)
print(np.mean(scores['test_score']))
print(np.mean(scores['fit_time']))

#축소 데이터를 이용해 KMeans 학습 진행
from sklearn.cluster import KMeans
km = KMeans(n_clusters=3, random_state=42)
km.fit(fruits_pca)
print(np.unique(km.labels_, return_counts=True))

for label in range(0, 3):
    draw_fruits(fruits[km.labels_==label])
    print()

#차원 축소시 좋은 점 : 데이터 크기적 이득, 시각화
for label in range(0, 3):
    data = fruits_pca[km.labels_==label]
    plt.scatter(data[:,0], data[:,1])
plt.legend(["pineapple", 'banana', 'apple'])
plt.show()