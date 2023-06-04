#패션 MNIST 데이터 사용
#텐서플로우 라이브러리 사용

from tensorflow import keras
(train_input, train_target), (test_input, test_target) = keras.datasets.fashion_mnist.load_data()

print(train_input.shape, train_target.shape)
print(test_input.shape, test_target.shape)

#이미지 시각화
import matplotlib.pyplot as plt
fig, axs = plt.subplots(1, 10, figsize=(10, 10))
for i in range(10):
    axs[i].imshow(train_input[i], cmap='gray_r')
    axs[i].axis('off')
plt.show()

#각 이미지들의 타깃값 확인
print(train_target[i] for i in range(10))

import numpy as np
#각 품목별 개수 확인
print(np.unique(train_target, return_counts=True))

#SGDClassifier 사용해볼 것 (선형 분류모델(경사하강법))
#이차원 배열을 받지 못하므로 1차원 배열로 reshape

train_scaled = train_input / 255.0
train_scaled = train_scaled.reshape(-1, 28*28)
print(train_scaled.shape)

#교차검증 라이브러리 사용
from sklearn.model_selection import cross_validate
from sklearn.linear_model import SGDClassifier

sc = SGDClassifier(loss='log', max_iter=5, random_state=42)
scores = cross_validate(sc, train_scaled, train_target, n_jobs=-1)
print(np.mean(scores['test_score']))

#텐서플로우 임포트 -> 인공신경망 사용을 위해
import tensorflow as tf

from sklearn.model_selection import train_test_split
train_scaled, val_scaled, train_target, val_target = train_test_split(train_scaled, train_target, test_size=0.2, random_state=42)

print(train_scaled.shape, train_target.shape)
print(val_scaled.shape, val_target.shape)

#양쪽 뉴런을 모두 연결하고 있는 층을 완전 연결층 이라고 부른다.
#케라스의 dense클래스
#keras.layers.Dense(10(뉴런의 개수), activation='softmax'(뉴런 출력에 사용될 함수), input_shape=(784,)(입력의 크기))
dense = keras.layers.Dense(10, activation='softmax', input_shape=(784,))
#신경망 층을 생성함
#밀집층을 가진 신경망 모델을 만들어야함 -> 케라스의 Sequential(dense) ->여기서 dense는 전에 만든 밀집층의 객체
model = keras.Sequential(dense) #Sequential클래스의 객체
#model 객체가 신경망 모델 (출력층 결과에 소프트맥스함수(활성화함수)를 적용해 결과 출력)

#케라스 모델 생성 방식은 다름
#훈련 전 설정 단계가 필요 -> compile()메서드 -> 필수로 지정해야 할 것 = 손실함수 -> 훈련과정에서 계산하고 싶은 측정값 지정

model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')
#sparse_categorical_crossentropy -> 전에 이진 분류에서 배웠던 손실함수 종류 (이진분류 : binary cross..., 다중분류 : categorical...)
#그럼 앞의 sparse는 뭘까? -> 다중분류 모델에서 cross entropy 손실함수를 사용할 때
# -> 손실율을 최대한 줄이기 위해 목표값을 제외한 모든 값을 0으로 -> 1번이 목표값이다 => [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# -> 손실율을 줄여?? 어떻게? -> 첫 번째 뉴런의 활성화 출력 a를 가능한 1에 가깝게 -> 위의 방법을 사용 (타겟 데이터를 변경)
# 이것이 원-핫 인코딩 (타깃값을 해당 클래스만 1이고 나머지가 0인 배열로 만드는 것)
#이 때 원-핫 인코딩을 하지 않고 타깃값이 정수인 상태로 사용할 수 있게 해주는 것이 sparse_... 이다.

#metrics 매개변수 먼가요?? -> 케라스는 기본적으로 훈련할 때 에포크마다 손실값을 출력해준다 -> 손실이 줄어드는 것을 보며 훈련 진행도 파악
# 정확도도 같이 보면 훨씬 좋음 -> 그래서 씀

#훈련 할 때는 .fit을 사용하지만 매개변수 epochs= 으로 훈련 반복 횟수 지정

model.fit(train_scaled, train_target, epochs=5)

#모델 검증할 때는 .evaluate()메서드 사용
model.evaluate(val_scaled, val_target)


#케라스 모델

# 1. 층 생성 : dense = keras.layers.Dense(10, activation='softmax', input_shape=(784,))
# 2. 모델 객체 생성 : model = keras.Sequential(dense)
# 3. 손실함수 지정 : model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')
# 4. 훈련 : model.fit(train_scaled, train_target, epochs=5)
# 5. 검증 : model.evaluate(val_scaled, val_target)
