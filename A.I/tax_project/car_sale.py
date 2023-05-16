import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('car_sales_data.csv')

data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d', errors='raise') #문자열인 날짜를 날짜 데이터식으로 변환

# maker = data['Car Make'].unique() #자동차 제조사
# cnt = data['Car Make'].value_counts() #제조사별 판매량
# #이 데이터는 닛산, 포드, 혼다, 토요타, 쉐보레 총 5개의 판매 데이터가 존재
#
# #시각화
# plt.figure(figsize=(10, 10))
#
# bar1 = plt.bar(maker, cnt)
#
# current_values = plt.gca().get_yticks()#지수표현 제거
# plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in current_values])#지수표현 제거
#
# for rect in bar1: #그래프 위 y값 표현
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2.0, height, height, ha='center', va='bottom', size = 12)
#
# plt.show()

# #연도별, 월별 판매량을 시각화
# df = pd.DataFrame()
# df['Year'] = data['Date'].dt.year
# df['Month'] = data['Date'].dt.month
# plt.figure(figsize=(10, 10))
#
# ax = df.groupby(['Year', 'Month']).value_counts().plot(kind='bar')#연도별, 월별 판매량 그래프화
#
# for p in ax.patches: #막대 그래프 위에 숫자 표기
#     ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom')
#
# plt.show()
#
# #판매가격 시각화
#
# plt.figure(figsize=(10,10))
# data['Sale Price'].plot(kind='bar')
# plt.show()

print(data)