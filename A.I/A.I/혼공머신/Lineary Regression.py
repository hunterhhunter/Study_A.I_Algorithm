import matplotlib.pyplot as plt
import numpy as np


perch_length = np.array([8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0, 21.0,
       21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5, 22.5, 22.7,
       23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5, 27.3, 27.5, 27.5,
       27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0, 36.5, 36.0, 37.0, 37.0,
       39.0, 39.0, 39.0, 40.0, 40.0, 40.0, 40.0, 42.0, 43.0, 43.0, 43.5,
       44.0])
perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0,
       115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0,
       150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0,
       218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0,
       556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0,
       850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0,
       1000.0])

from sklearn.model_selection import train_test_split

#훈련세트, 테스트세트 분할
train_input, test_input, train_target, test_target = train_test_split(perch_length, perch_weight, random_state=42)

# #2차원배열 변환
train_input = train_input.reshape(-1, 1)
test_input = test_input.reshape(-1, 1)
#
# from sklearn.neighbors import KNeighborsRegressor
#
# knr = KNeighborsRegressor(n_neighbors=3)
#
# #훈련진행
# knr.fit(train_input, train_target)
#
# #길이가 50인 농어 무게 예측
# print(knr.predict([[50]]))
#
# import matplotlib.pyplot as plt
#
# #길이 50인 농어 이웃 구하기
# distances, indexes = knr.kneighbors([[50]])
# plt.scatter(train_input, train_target)
# #훈련세트 중 이웃 샘플만 다시 그리기
# plt.scatter(train_input[indexes], train_target[indexes], marker='D')
#
# #길이 50 농어 데이터
# plt.scatter(50, 1033, marker='^')
# plt.xlabel("length")
# plt.ylabel('weight')
# plt.show()
#
# print(np.mean(train_target[indexes]))
#
# from sklearn.linear_model import LinearRegression
# lr = LinearRegression()
# lr.fit(train_input, train_target)
#
# print(lr.predict([[50]]))
#
# print(lr.coef_, lr.intercept_)
#
# plt.scatter(train_input, train_target)
#
# plt.plot([15, 50], [15*lr.coef_+lr.intercept_, 50*lr.coef_+lr.intercept_])
#
# plt.scatter(50, 1241.8, marker='^')
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()
#
# print(lr.score(train_input, train_target))
# print(lr.score(test_input, test_target))
#
# train_poly = np.column_stack((train_input**2, train_input))
# test_poly = np.column_stack((test_input**2, test_input))
#
# print(train_poly.shape, test_poly.shape)
#
# lr = LinearRegression()
# lr.fit(train_poly, train_target)
# print(lr.predict([[50**2, 50]]))
# print(lr.coef_, lr.intercept_)
#
# point = np.arange(15, 50)
#
# plt.scatter(train_input, train_target)
# plt.plot(point, 1.014*point**2 -21.55*point + 116.05)
# plt.scatter([50], [1574], marker='^')
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()

import pandas as pd
df = pd.read_csv('https://bit.ly/perch_csv_data')
perch_full = df.to_numpy()
print(perch_full)

from sklearn.preprocessing import PolynomialFeatures

train_input, test_input, train_target, test_target = train_test_split(perch_full, perch_weight, random_state=42)

poly = PolynomialFeatures() #특성들을 다양하게 추가 -> 각 항의 곱, 제곱을 추가해줌 -> 특성이 많을수록 선형회귀는 좋음
poly.fit([[2, 3]])
print(poly.transform([[2, 3]]))

poly = PolynomialFeatures(include_bias=False)
poly.fit([[2, 3]])
print(poly.transform([[2, 3]]))

poly = PolynomialFeatures(include_bias=False)
poly.fit(train_input)
train_poly = poly.transform(train_input)
print(train_poly.shape)

print(poly.get_feature_names_out()) #각각의 특성 출력

test_poly = poly.transform(test_input)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(train_poly, train_target)
print(lr.score(train_poly, train_target))
print(lr.score(test_poly, test_target))

poly = PolynomialFeatures(degree=5, include_bias=False)
poly.fit(train_input)
train_poly = poly.transform(train_input)
test_poly = poly.transform(test_input)
print(train_poly.shape)

lr.fit(train_poly, train_target)
print(lr.score(train_poly, train_target))
print(lr.score(test_poly, test_target))

from sklearn.preprocessing import StandardScaler #스케일러로 표준점수로 변환시킬 수 있음 -> 각종 규제 전에 필수적
ss = StandardScaler()
ss.fit(train_poly)
train_scaled = ss.transform(train_poly)
test_scaled = ss.transform(test_poly)

from sklearn.linear_model import Ridge #릿지 회귀는 계수를 제곱한 값을 기준으로 규제 적용
ridge = Ridge()
ridge.fit(train_scaled, train_target)
print(ridge.score(train_scaled, train_target))
print(ridge.score(test_scaled, test_target))

import matplotlib.pyplot as plt
train_score = []
test_score = []

alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]
for alpha in alpha_list:
       ridge = Ridge(alpha=alpha)
       ridge.fit(train_scaled, train_target)
       train_score.append(ridge.score(train_scaled, train_target))
       test_score.append(ridge.score(test_scaled, test_target))
plt.plot(np.log10(alpha_list), train_score)
plt.plot(np.log10(alpha_list), test_score)
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.show()

ridge = Ridge(alpha=0.1)
ridge.fit(train_scaled, train_target)
print(ridge.score(train_scaled, train_target))
print(ridge.score(test_scaled, test_target))

from sklearn.linear_model import Lasso #라쏘 회귀는 계수의 절댓값을 기준으로 규제 적용
lasso = Lasso()
lasso.fit(train_scaled, train_target)
print(lasso.score(train_scaled, train_target))
print(lasso.score(test_scaled, test_target))

train_score = []
test_score = []

alpha_list = np.arange(0.01, 10, 0.01)
for alpha in alpha_list:
       lasso = Lasso(alpha=alpha, max_iter=10000)
       lasso.fit(train_scaled, train_target)
       train_score.append(lasso.score(train_scaled, train_target))
       test_score.append(lasso.score(test_scaled, test_target))
plt.plot(np.log10(alpha_list), train_score)
plt.plot(np.log10(alpha_list), test_score)
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.show()

lasso = Lasso(alpha=10)
lasso.fit(train_scaled, train_target)
print(lasso.score(train_scaled, train_target))
print(lasso.score(test_scaled, test_target))

#모델 계수를 살펴보며 0이된 것 파악
print(np.sum(lasso.coef_==0))