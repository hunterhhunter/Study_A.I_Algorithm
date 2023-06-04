from tensorflow import keras
(train_input, train_target), (test_input, test_target) = keras.datasets.fashion_mnist.load_data()

train_scaled = train_input / 255.0
train_scaled = train_scaled.reshape(-1, 28*28)
from sklearn.model_selection import train_test_split
train_scaled, val_scaled, train_target, val_target = train_test_split(train_scaled, train_target, test_size=0.2, random_state=42)

# 신경망 모델에 층을 2개 추가
# 은닉층을 추가할 것 -> 은닉층에 활성화 함수가 존재 -> 왜? -> 선형적인 산술계산만 한다면 은닉층이 의미가 없음
# -> 결과를 비틀어 은닉층을 의미있게

dense1 = keras.layers.Dense(100, activation='sigmoid', input_shape=(784,)) #은닉층
dense2 = keras.layers.Dense(10, activation='softmax') #출력층

#심층 신경망 생성
model = keras.Sequential([dense1, dense2])
#케라스의 장점은 층을 여러 개 만들어 바복적인 학습이 존재하기 때문

# 모델의 층에 대한 정보가 궁금하다면 summary() 메서드 호출
model.summary()

#output shape에서 None인 이유? -> 케라스의 fit 메서드는 훈련데이터를 한 번에 모두 사용하지 않고 나누어 사용하여 여러번의 경사하강법 진행
# -> 미니배치 경사 하강법
#각 뉴런마다 각 한개의 절편이 존재한다는 것을 잊지 말자!
#Non-trainable params는 경사하강법으로 훈련되지 않는 파라미터를 가진 층이 존재

#층을 추가하는 방법 -> 보통 Dense의 객체 dense1, dense2를 따로 저장하여 사용하지 않기 때문에 생성자 안에 바로 객체를 넣는다.
model = keras.Sequential([keras.layers.Dense(100, activation='sigmoid', input_shape=(784,), name='hidden'),
                         keras.layers.Dense(10, activation='softmax', name='output')],
                         name='패션 MNIST 모델')
#추가되는 층을 한눈에 볼 수 있음
model.summary()

#근데 층이 많아지면 불편함 -> add메서드

model = keras.Sequential()
model.add(keras.layers.Dense(100, activation='sigmoid', input_shape=(784,), name='hidden'))
model.add(keras.layers.Dense(10, activation='softmax', name='output'))

model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')
model.fit(train_scaled, train_target, epochs=5)

#이미지 분류에 높은 성능을 내는 렐루 함수
# 기존의 시그모이드 함수는 양 끝으로 갈 수록 변화가 작기 때문에 올바른 출력을 만드는데 신속하지 못하다
# -> 그래서 나온게 렐루함수 -> 렐루함수는 출력이 양수일 때 그냥 입력을 통과 but 음수일 때는 0을 출력 -> 렐루함수는 max(0, z)로 표현 가능

#케라스에는 입력 데이터를 직접 reshape 할 필요없이 Flatten 클래스가 존재한다. -> 배치 차원을 제외한 모든 입력 차원을 일렬로 펼치는 역할만
#성능에 기여하는 바는 없음 -> 층처럼 입력층과 은닉층 사이에 추가하기 때문에 이를 층이라 부른다.

model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(28, 28)))
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))

model.summary()

(train_input, train_target), (test_input, test_target) = keras.datasets.fashion_mnist.load_data()
train_scaled = train_input / 255.0
train_scaled, val_scaled, train_target, val_target = train_test_split(train_scaled, train_target, test_size=0.2, random_state=42)


model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')
model.fit(train_scaled, train_target, epochs=5)

model.evaluate(val_scaled, val_target)

#옵티마이저
#케라스에는 다양한 하이퍼파라미터가 존재 -> 은닝층 개수, 종류, 미니배치 사이즈, 경사하강법 알고리즘 등등...
#케라스의 미니배치 경사하강법의 미니배치는 32개, 다양한 경사하강법 알고리즘들을 옵티마이저라고 한다.
#여러개의 옵티마이저를 실험해볼 것
#SGD(확률적 경사 하강법) - 이름만 SGD고 미니배치 사용
model.compile(optimizer='sgd', loss='sparse_categorical_crossentropy', metrics='accuracy')
#여기서 'sgd'랑 sgd랑 차이가 뭔가요? 'sgd'는 따로 SGD 객체를 만들 필요 없이 자동으로 객체를 만들어줌

sgd = keras.optimizers.SGD(learning_rate=0.1)
#학습률 변경

#모멘텀 최적화
#기존 경사 하강법에는 한계가 존재
# 1. Local Minimum 문제 -> 최적의 값이라고 판단한 값이 정말 최솟값인지 알 수 없다 ex: 양 아래 변곡점의 위치가 다른 4차함수 그래프
# 2. Saddle Point 문제 -> 안장점을 벗어나지 못함 -> 미분이 0일 경우 멈추기 때문에
# -> 어떤 경로에서는 최솟값이지만 어떤 경로에서는 최댓값일 수 있다
# => 이를 극복하기 위한 모멘텀(관성) 최적화 -> 경사하강법에 관성을 적용해 전의 기울기에 따라 추가적으로 움직여 전의 문제들을 해결할 수 있다
#nesterov 모멘텀 최적화를 사용하면 모멘텀 최적화를 2번 반복 진행해 더 나은 성능
# -> 모델이 최적점에 가까이 갈수록 학습률을 낮출 수 있다 -> 안정적으로 최적점에 수렴 -> 적응정 학습률 -> 학습률 매개변수 튜닝하는 수고 줄임
# Adagrad, RMSprop -> 옵티마이저 변수의 기본값이 rmsprop임
sgd = keras.optimizers.SGD(momentum=0.9, nesterov=True)

adagrad = keras.optimizers.Adagrad()
model.compile(optimizer=adagrad, loss='sparse_categorical_crossentropy', metrics='accuracy')

rmsprop = keras.optimizers.RMSprop()
model.compile(optimizer=rmsprop, loss='sparse_categorical_crossentropy', metrics='accuracy')

#이렇게 사용 가능

model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(28, 28)))
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')
model.fit(train_scaled, train_target, epochs=5)

model.evaluate(val_scaled, val_target)