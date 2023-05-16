import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("Delayed_tax.csv", encoding='euc-kr')


#전처리
data_rigion = data[0:17]
data_columns = data[17:-1]

data_rigion = data_rigion.drop(['구분1'], axis=1)
data_columns = data_columns.drop(['구분1'], axis=1)
#인덱스번호 리셋
data_columns = data_columns.reset_index()
#컬럼명 변경
data_rigion = data_rigion.rename(columns={'구분2':'지역'})
data_columns = data_columns.rename(columns={'구분2':'세목'})

#단위 100만에서 1000원으로 변경
col_name = list(data_rigion.columns)
col_name1 = list(data_columns.columns)
for col in col_name:
    if '금액' in col:
        data_rigion[col] = data_rigion[col] * 1000
for col in col_name1:
    if '금액' in col:
        data_columns[col] = data_columns[col] * 1000

data_rigion['발생 건수당 평균 금액'] = data_rigion['2022년 발생금액']/data_rigion['2022년 발생건수']
data_columns['발생 건수당 평균 금액'] = data_columns['2022년 발생금액']/data_columns['2022년 발생건수']

plt.figure(figsize=(20, 16))#(단위:1000원)
plt.rcParams['font.family'] ='Malgun Gothic' #matplotlib에서 한글 보기위해 사용
plt.rcParams['axes.unicode_minus'] =False

plt.subplot(121)
bar1 = plt.bar(data_rigion['지역'], data_rigion['2022년 발생금액'])

current_values = plt.gca().get_yticks()#지수표현 제거
plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in current_values])#지수표현 제거

# for rect in bar1: #그래프 위 y값 표현
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2.0, height, height, ha='center', va='bottom', size = 12)

plt.subplot(122)
bar2 = plt.bar(data_columns['세목'], data_columns['2022년 발생금액'])

current_values = plt.gca().get_yticks()#지수표현 제거
plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in current_values])#지수표현 제거

for rect in bar2: #그래프 위 y값 표현
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, height, ha='center', va='bottom', size = 12)

plt.show()

#발생 건수당 평균 금액(단위:1000원)
plt.figure(figsize=(20, 16))
plt.rcParams['font.family'] ='Malgun Gothic' #matplotlib에서 한글 보기위해 사용
plt.rcParams['axes.unicode_minus'] =False

plt.subplot(121)
bar1 = plt.bar(data_rigion['지역'], data_rigion['발생 건수당 평균 금액'])

current_values = plt.gca().get_yticks()#지수표현 제거
plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in current_values])#지수표현 제거

for rect in bar1: #그래프 위 y값 표현
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.2f' %height, ha='center', va='bottom', size = 12)

plt.subplot(122)
bar2 = plt.bar(data_columns['세목'], data_columns['발생 건수당 평균 금액'])

current_values = plt.gca().get_yticks()#지수표현 제거
plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in current_values])#지수표현 제거

for rect in bar2: #그래프 위 y값 표현
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.2f' %height, ha='center', va='bottom', size = 12)

plt.show()

print(data_rigion)
print(data_columns)