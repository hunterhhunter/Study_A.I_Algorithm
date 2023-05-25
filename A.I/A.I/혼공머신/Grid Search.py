#교차검증과 그리드 서치
#테스트 세트를 이용해 계속 평가시 테스트 세트에 맞는 모델이 될 수 있다
#그래서 검증 세트를 추가하여 테스트 세트의 사용을 최소화
import pandas as pd
wine = pd.read_csv("https://bit.ly/wine_csv_data")

data = wine[['alcohol', 'sugar', 'pH']].to_numpy()
target = wine['class'].to_numpy()

from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(data, target,test_size=0.2, random_state=42)

sub_input, val_input, sub_target, val_target = train_test_split(train_input, train_target, test_size=0.2, random_state=42)

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(random_state=42)
dt.fit(sub_input, sub_target)
print(dt.score(sub_input, sub_target))
print(dt.score(val_input, val_target))

#교차검증 - K-겹 교차검증
#훈련세트를 K개로 나누어 하나씩 돌아가며 검증세트로 사용 -> 안정적인 검증 점수 -> 보통은 5 or 10 - 폴드 교차검증
#교차 검증 모델인 cross_validate
#cross_val_score를 사용해 점수만 가져올 수 있음
from  sklearn.model_selection import cross_validate
scores = cross_validate(dt, train_input, train_target)
print(scores)

import numpy as np
print(np.mean(scores['test_score'])) #교차검증 점수의 평균

#cross_validate 함수는 기본적으로 회귀일시 KFOLD 분할기, 분류일시 StratifiedKFold를 사용한다.
#앞에서 진행한 교차검증은 다음과 같다.
from sklearn.model_selection import StratifiedKFold
scores = cross_validate(dt, train_input, train_target, cv=StratifiedKFold())
print(np.mean(scores['test_score']))

#10-폴드 교차 검증을 하려면
splitter = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
scores = cross_validate(dt, train_input, train_target, cv=splitter)
print(np.mean(scores['test_score']))

#하이퍼 파라미터를 직접 찾는게 아닌 GridSearchCV 클래스를 호출해 사용 -> 하이퍼 파라미터 탐색 자동화
from sklearn.model_selection import GridSearchCV
params = {'min_impurity_decrease':[0.0001, 0.0002, 0.0003, 0.0004, 0.0005]}
gs = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1) #n_jobs는 사용할 코어 개수 -1은 전부

gs.fit(train_input, train_target) #결정트리 모델로 params의 개수 5 * (그리드서치의 기본 분할 5분할) = 25번의 모델을 훈련
dt = gs.best_estimator_ #최고의 모델을 호출
print(dt.score(train_input, train_target))
print(gs.best_params_) #각 파라미터중 성능이 가장 좋은 값
print(gs.cv_results_['mean_test_score']) #교차검증의 각 값들 -> 그 중 교차검증의 평균점수

#최상의 검증 점수를 만든 매개변수 조합
best_index = np.argmax(gs.cv_results_['mean_test_score'])
print(gs.cv_results_['params'][best_index])

'''조금 더 복잡한 매개변수 조합'''
params = {'min_impurity_decrease':np.arange(0.0001, 0.001, 0.0001),
          'max_depth' : range(5, 20, 1),
          'min_samples_split':range(2, 100, 10)
          }
gs = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1)
gs.fit(train_input, train_target)

print(gs.best_params_)
print(np.max(gs.cv_results_['mean_test_score']))

#랜덤 서치
from scipy.stats import uniform, randint
#uniform은 실수 randint는 정수를 범위 내에서 균등분포에서 샘플링한다. -> 확률이 모두 같다
rgen = randint(0, 10)
rgen.rvs(10)

np.unique(rgen.rvs(1000), return_counts=True)
#실수집합
ugen = uniform(0, 1)
ugen.rvs(10)

'''난수로 매개변수 탐색하기'''
params = {'min_impurity_decrease':uniform(0.0001, 0.001),
          'max_depth' : randint(20, 50),
          'min_samples_split': randint(2, 25),
          'min_samples_leaf': randint(1, 25)
          }

from sklearn.model_selection import RandomizedSearchCV
gs = RandomizedSearchCV(DecisionTreeClassifier(splitter='random', random_state=42), params, n_iter=100, n_jobs=-1, random_state=42)
gs.fit(train_input, train_target)

print(gs.best_params_)

print(np.max(gs.cv_results_['mean_test_score']))

dt = gs.best_estimator_
print(dt.score(test_input, test_target))