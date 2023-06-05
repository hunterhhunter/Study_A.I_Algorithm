from tensorflow import keras
(train_input, train_target), (test_input, test_target) = keras.datasets.fashion_mnist.load_data()

train_scaled = train_input / 255.0
from sklearn.model_selection import train_test_split
train_scaled, val_scaled, train_target, val_target = train_test_split(train_scaled, train_target, test_size=0.2, random_state=42)

#모델을 생성하는 간단한 함수 생성
def model_fn(a_layer=None):
    model = keras.Sequential()
    model.add(keras.layers.Flatten(input_shape=(28, 28)))
    model.add(keras.layers.Dense(100, activation='relu'))
    if a_layer: #a_layer이 들어올 경우 층을 하나 더 만들어 준다 -> 입력 변수가 모델이겠지?
        model.add(a_layer)
    model.add(keras.layers.Dense(10, activation='softmax'))
    return model

model = model_fn()
model.summary()

# .fit() 메서드는 훈련 과정에서 계산한 손실, 정확도 값이 저장되어 있는 객체를 반환
model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')
history = model.fit(train_scaled, train_target, epochs=5, verbose=0) #verbose 는 훈련과정 출력할지 0:x 1:o 2:막대 제외
print(history.history.keys())

import matplotlib.pyplot as plt
plt.plot(history.history['loss'])
plt.xlabel('epochs')
plt.ylabel('loss')
plt.show()

plt.plot(history.history['accuracy'])
plt.xlabel('epochs')
plt.ylabel('loss')
plt.show()

#에포크 20으로 늘려서 진행

model = model_fn()
model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')
history = model.fit(train_scaled, train_target, epochs=20, verbose=0)
plt.plot(history.history['loss'])
plt.xlabel('epochs')
plt.ylabel('loss')
plt.show()

#검증 손실
#신경망 또한 일종의 경사하강법을 통해 학습 -> 어떤 모델은 손실 감소에 비례하여 정확도가 높아지지 않을 수 있기 때문에 훈련정도를 파악하려면
# 정확도 보다는 손실함수의 값을 확인하는게 더 좋다.

#에포크마다 검증손실을 계산하기위해 검증 데이터를 튜플 형태로 전달해줌
model = model_fn()
model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')
history = model.fit(train_scaled, train_target, epochs=20, verbose=0,
                    validation_data=(val_scaled, val_target))

print(history.history.keys())

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()

# 5에포크를 넘어갈 때 부터 검증세트 손실값이 점점 커진다. -> 옵티마이저 하이퍼파라미터를 조정해 과대적합을 완화
# 그중 Adam 을 사용 -> 적응적 학습률을 사용하기 때문에 에포크가 진행되면서 학습률의 크기를 조정 가능

model = model_fn()
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')
history = model.fit(train_scaled, train_target, epochs=20, verbose=0,
                    validation_data=(val_scaled, val_target))

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()

#드롭 아웃 -> 층에 있는 일부 뉴런을 랜덤하게 꺼서(출력을 0으로 만듬) 과대적합을 막는다.
# 얼마나 많은 뉴런을 끌지는 직접 정해야함
# 이게 왜 과대적합을 막아줄까? -> 일부 뉴런에 과대하게 의존하는 것을 줄일 수 있고 모든 입력에 주의를 기울여야 한다.

#케라스에 Dropout 클래스를 제공

model = model_fn(keras.layers.Dropout(0.3))
model.summary()

#그럼 검증, 평가때는 드롭아웃 하면 안되지 않나? -> 자동으로 해줌

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')
history = model.fit(train_scaled, train_target, epochs=20, verbose=0,
                    validation_data=(val_scaled, val_target))

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()

# 10회정도 일 때 과대적합이 가장 잘 줄은 것을 볼 수 있다.

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')
history = model.fit(train_scaled, train_target, epochs=10, verbose=0,
                    validation_data=(val_scaled, val_target))

#모델 저장과 복원
#모델을 저장하는 방법은 훈련된 모델의 파라미터를 저장하는 save_weight라는 메스드를 제공
model.save_weights('model-weight.h5')
#모델 구조와 파라미터를 함께 저장하는 save메서드도 제공
model.save('model-whole.h5')

#그럼 이 모델을 어떻게 복원하지? -> load_weight() 메서드

model = model_fn(keras.layers.Dropout(0.3))
model.load_weights('model-weight.h5')

#모델 파라미터를 읽은 후 evaluate 메서드를 사용해 정확도를 출력할 수 있지만 이를 사용하기 위해 compile 메서드를 꼭 사용해야 하기에
# 새로운 데이터에 대한 정확도만 계산하면 되는 상황으로 가정
# => 파라미터만을 불러들였기 때문에 모델 구조가 다르면 사용하지 못할 뿐더러 컴파일을 한 번 더 해야해서 안됨
import numpy as np
val_labels = np.argmax(model.predict(val_scaled), axis=-1)
print(np.mean(val_labels==val_target))

#예측 결과에서 가장 큰 값을 고르기 위해 argmax를 사용했고 axis가 -1인 이유는 배열의 마지막 차원을 따라 최댓값을 고른다.
# -> 검증세트는 2차원 배열이기 때문에 마지막 차원은 1이 된다.
# 그리고 예측값과 정답이 맞는지 확인해 평균내면 정확도가 된다.

model = keras.models.load_model('model-whole.h5')
model.evaluate(val_scaled, val_target)

#둘은 같은 모델이기 때문에 같은 정확도


#콜백 : 훈련 과정중간에 어떤 작업을 수행할 수 있게 해주는 객체로 callback 패키지 아래에 있음
#ex : ModelCheckpoint 콜백은 에포크 마다 모델을 저장한다.
#save_best_only=True 로 지정하여 가장 낮은 검증 저수를 모델을 저장할 수 있다.

model = model_fn(keras.layers.Dropout(0.3))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')
checkpoint_cb = keras.callbacks.ModelCheckpoint('best-model.h5', save_best_only=True)
model.fit(train_scaled, train_target, epochs=20, verbose=0,
          validation_data=(val_scaled, val_target), callbacks=[checkpoint_cb])

#모델 불러오기
model = keras.models.load_model('best-model.h5')
model.evaluate(val_scaled, val_target)

# 그래도 20번 훈련하는 것은 마찬가지다 -> 조기에 종료해서 과대적합을 막는 것 => 조기종료
# EarlyStopping 콜백을 제공 -> patience=n n번동안 검증 점수가 향상되지 않으면 조기 종료함
# EarlyStopping 콜백과 ModelCheckpoint 콜백을 사용하면 가장 낮은 검증 손실의 모델을 파일에 저장하고
# 검증 손실이 다시 상승할 때 훈련을 중지할 수 있다. -> 훈련 중지 후 최상의 파라미터로 되돌릴 수 있다.

model = model_fn(keras.layers.Dropout(0.3))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')
checkpoint_cb = keras.callbacks.ModelCheckpoint('best-model.h5', save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=2, restore_best_weights=True)
history = model.fit(train_scaled, train_target, epochs=20, verbose=0,
          validation_data=(val_scaled, val_target), callbacks=[checkpoint_cb, early_stopping_cb])

#언제 학습을 멈췄는지 보기
print(early_stopping_cb.stopped_epoch)

#조기종료 한 모델의 검증세트 성능 확인
model.evaluate(val_scaled, val_target)