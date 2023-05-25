#앙상블 학습 모델은 하나의 강력한 모델을 사용하는 대신 작은 여러 개의 분류 모델들을 결합하여 더 정확한 예측에 도움을 주는 방식
#랜덤 포레스트 분류 모델
#부트스트랩 샘플 -> 데이터를 뽑을 때 중복을 허용하여 뽑아서 데이터셋을 형성함
#랜덤 포레스트 분류 모델은 전체 특성의 개수의 제곱근만큼 특성을 선택해 부트스트랩 샘플 생성
import numpy as np
import pandas as pd
wine = pd.read_csv("https://bit.ly/wine_csv_data")

data = wine[['alcohol', 'sugar', 'pH']].to_numpy()
target = wine['class'].to_numpy()
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(data, target,test_size=0.2, random_state=42)

from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_jobs=-1, random_state=42)
scores = cross_validate(rf, train_input, train_target, return_train_score=True, n_jobs=-1)
print(np.mean(scores['train_score']), np.mean(scores['test_score']))

rf.fit(train_input, train_target)
print(rf.feature_importances_)
#oob(out of bag) 부트스트랩 샘플을 생성하고 선택받지 못한 나머지 데이터들의 집합을 이용해 검증 샘플을 생성하여 평가할 수 있다.
rf = RandomForestClassifier(oob_score=True, n_jobs=-1, random_state=42)
rf.fit(train_input, train_target)
print(rf.oob_score_)

#엑스트라 트리 -> 부트스트랩 샘플 사용하지 않음 대신 노드를 분할할 때 정보이득이 커지는 분할이 아닌 무작위 분할
# -> 그래서 계산 속도가 빠름
from sklearn.ensemble import ExtraTreesClassifier
et = ExtraTreesClassifier(n_jobs=-1, random_state=42)
scores = cross_validate(et, train_input, train_target, return_train_score=True, n_jobs=-1)
print(np.mean(scores['train_score']), np.mean(scores['test_score']))

et.fit(train_input, train_target)
print(et.feature_importances_)

#그레이디언트 부스팅-> 경사하강법 원리를 이용 -> 결정트리를 계속 추가하며 가장 낮은 곳을 찾아 이동 -> 그렇기에 깊이가 얕은 트리를 이용
#과대적합에 강함
from sklearn.ensemble import GradientBoostingClassifier
gb = GradientBoostingClassifier(random_state=42)
scores = cross_validate(gb, train_input, train_target, return_train_score=True, n_jobs=-1)
print(np.mean(scores['train_score']), np.mean(scores['test_score']))
#학습률, 트리개수 설정
gb = GradientBoostingClassifier(n_estimators=500, learning_rate=0.2, random_state=42)
scores = cross_validate(gb, train_input, train_target, return_train_score=True, n_jobs=-1)
print(np.mean(scores['train_score']), np.mean(scores['test_score']))

gb.fit(train_input, train_target)
print(gb.feature_importances_)

#히스토그램 기반 그레이디언트 부스팅
#입력특성을 256구간으로 분할 -> 노드 분할시 최적의 분할을 빠르게 찾을 수 있음 (256개의 구간중 하나를 떼어두고 누락값을 위해 사용)

from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingClassifier
hgb = HistGradientBoostingClassifier(random_state=42)
scores = cross_validate(hgb, train_input, train_target, return_train_score=True)
print(np.mean(scores['train_score']), np.mean(scores['test_score']))

from sklearn.inspection import permutation_importance

hgb.fit(train_input, train_target)
result = permutation_importance(hgb, train_input, train_target, n_repeats=10, random_state=42, n_jobs=-1)
#permutation_importance 함수가 반환하는 객체는 반복하여 얻은 각 특성의 중요도, 중요도 평균, 중요도 표준편차를 가지고 있다.
print(result.importances_mean)

hgb.fit(train_input, train_target)
result = permutation_importance(hgb, test_input, test_target, n_repeats=10, random_state=42, n_jobs=-1)
#permutation_importance 함수가 반환하는 객체는 반복하여 얻은 각 특성의 중요도, 중요도 평균, 중요도 표준편차를 가지고 있다.
print(result.importances_mean)

print(hgb.score(test_input, test_target))
#또 다른 히스토그램 기반 그레이디언트 부스팅 라이브러리
#xgboost, lightgbm 모두 cross_validate와 연계하여 사용 가능