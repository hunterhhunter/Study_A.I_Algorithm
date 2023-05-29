import numpy as np
import matplotlib.pyplot as plt

fruits = np.load('fruits_300.npy')
print(fruits.shape)
print(fruits[0, 0, :])
#넘파이 배열로 저장된 이미지를 나타낼 수 있다.
plt.imshow(fruits[0], cmap='gray') #흑백그림이기에 gray
plt.show()
#색에 반전을 줌 -> 흰색은 값이 0에 가까운데 0에는 어떤 처리를 하더라도 0이기 때문에 색 반전을 통해 255와 가깝게 변환
plt.imshow(fruits[0], cmap='gray_r')
plt.show()

fig, axs = plt.subplots(1, 2)
axs[0].imshow(fruits[100], cmap='gray_r')
axs[1].imshow(fruits[200], cmap='gray_r')
plt.show()

#각 100 * 100의 이미지들을 10,000개의 요소를 가진 하나의 배열로 바꿈
apple = fruits[0:100].reshape(-1, 100*100)
pineapple = fruits[100:200].reshape(-1, 100*100)
banana = fruits[200:300].reshape(-1, 100*100)

print(apple.shape)
#평균값 구하기
print(apple.mean(axis=1))

plt.hist(np.mean(apple, axis=1), alpha=0.8)
plt.hist(np.mean(pineapple, axis=1), alpha=0.8)
plt.hist(np.mean(banana, axis=1), alpha=0.8)

plt.legend(['apple', 'pineapple', 'banana'])
plt.show()
#전체 샘플에 대해 각 픽셀의 평균을 구하기 -> 각 과일마다 픽셀값이 높은 위치가 다르다.
fig, axs = plt.subplots(1, 3, figsize=(20,5))
axs[0].bar(range(10000), np.mean(apple, axis=0))
axs[1].bar(range(10000), np.mean(pineapple, axis=0))
axs[2].bar(range(10000), np.mean(banana, axis=0))
plt.show()

apple_mean = np.mean(apple, axis=0).reshape(100, 100)
pineapple_mean = np.mean(pineapple, axis=0).reshape(100, 100)
banana_mean = np.mean(banana, axis=0).reshape(100, 100)
fig, axs = plt.subplots(1, 3, figsize=(20, 5))
axs[0].imshow(apple_mean, cmap='gray_r')
axs[1].imshow(pineapple_mean, cmap='gray_r')
axs[2].imshow(banana_mean, cmap='gray_r')
plt.show()
#사과의 평균값 배열과 전체 과일 배열의 차이를 이용해 사과를 골라낼 수 있다 -> 0에 수렴할수록 사과와 유사하다는 뜻
#각 픽셀의 유사도를 평균내서 abs_mean에 저장 -> 낮을수록 사과일 확률 up
abs_diff = np.abs(fruits-apple_mean)
abs_mean = np.mean(abs_diff, axis=(1,2))
print(abs_mean.shape)
#argsort함수는 작은것에서 큰 순서대로 나열한 배열의 인덱스를 반환 -> 이들 중 처음 100개는 사과와 유사한 것이겠지?
apple_index = np.argsort(abs_mean)[:100]
fig, axs = plt.subplots(10, 10, figsize=(10,10))
for i in range(10):
    for j in range(10):
        axs[i, j].imshow(fruits[apple_index[i*10+j]], cmap='gray_r')
        axs[i, j].axis('off')
plt.show()

abs_diff = np.abs(fruits-pineapple_mean)
abs_mean = np.mean(abs_diff, axis=(1,2))
pineapple_index = np.argsort(abs_mean)[:100]
fig, axs = plt.subplots(10, 10, figsize=(10,10))
for i in range(10):
    for j in range(10):
        axs[i, j].imshow(fruits[pineapple_index[i*10+j]], cmap='gray_r')
        axs[i, j].axis('off')
plt.show()

abs_diff = np.abs(fruits-banana_mean)
abs_mean = np.mean(abs_diff, axis=(1,2))
banana_index = np.argsort(abs_mean)[:100]
fig, axs = plt.subplots(10, 10, figsize=(10,10))
for i in range(10):
    for j in range(10):
        axs[i, j].imshow(fruits[banana_index[i*10+j]], cmap='gray_r')
        axs[i, j].axis('off')
plt.show()

