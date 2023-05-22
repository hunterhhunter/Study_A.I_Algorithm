import pandas as pd
fish = pd.read_csv('https://bit.ly/fish_csv_data')
print(fish.head())

print(fish['Species'].unique())

fish_input = fish[['Weight', 'Length', 'Diagonal', 'Height', 'Width']].to_numpy()

print(fish_input[:5])
fish_target = fish['Species'].to_numpy()

from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(fish_input, fish_target, random_state=42)

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(train_scaled, train_target)
print(knn.score(train_scaled, train_target))
print(knn.score(test_scaled, test_target))

#사이킷런에서 타깃값이 문자열일경우 순서가 알파벳순으로 자동변환 -> 각 생선의 데이터가 달라질 수 있음
print(knn.classes_)

print(knn.predict(train_scaled[:5]))

import numpy as np
proba = knn.predict_proba(test_scaled[:5])
print(np.round(proba, decimals=4))

distances, indexes = knn.kneighbors(test_scaled[3:4])
print(train_target[indexes])

import matplotlib.pyplot as plt
z = np.arange(-5, 5, 0.1)
phi = 1 / (1+np.exp(-z))
plt.plot(z, phi)
plt.xlabel('z')
plt.ylabel('phi')
plt.show()

bream_smelt_indexes = (train_target == 'Brea'
                                       ''
                                       ''
                                       ''
                                       'm') | (train_target == 'Smelt')
train_bream_smelt = train_scaled[bream_smelt_indexes]
target_bream_smelt = train_target[bream_smelt_indexes]

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(train_bream_smelt, target_bream_smelt)

print(lr.predict(train_bream_smelt[:5]))
print(lr.predict_proba(train_bream_smelt[:5]))

print(lr.coef_, lr.intercept_)

dicisions = lr.decision_function(train_bream_smelt[:5])
print(dicisions)

from scipy.special import  expit #시그모이드 함수 사용을 위해
print(expit(dicisions))