import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('car_sales_data.csv')

data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d', errors='raise') #문자열인 날짜를 날짜 데이터식으로 변환

unique_car_makes = data['Car Make'].unique()
unique_car_models = data['Car Model'].unique()

print("Unique Car Makes: \n", unique_car_makes)
print("Unique Car Models: \n", unique_car_models)
#
car_make_counts = data['Car Make'].value_counts()
print(car_make_counts)
#
car_model_counts = data['Car Model'].value_counts()
print(car_model_counts)
#
car_model_perc = data['Car Model'].value_counts(normalize=True) * 100
print(car_model_perc)
#
car_make_perc = data['Car Make'].value_counts(normalize=True) * 100
print(car_make_perc)

#이 데이터는 닛산, 포드, 혼다, 토요타, 쉐보레 총 5개의 판매 데이터가 존재

#시각화
plt.figure(figsize=(10, 10))
plt.subplot(121)
bar1 = plt.bar(unique_car_makes, car_make_counts)

current_values = plt.gca().get_yticks()#지수표현 제거
plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in current_values])#지수표현 제거

for rect in bar1: #그래프 위 y값 표현
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, height, ha='center', va='bottom', size = 12)

plt.subplot(122)
bar2 = plt.bar(unique_car_models, car_model_counts)

current_values = plt.gca().get_yticks()#지수표현 제거
plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in current_values])#지수표현 제거

for rect in bar2: #그래프 위 y값 표현
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, height, ha='center', va='bottom', size = 12)

plt.show()

#연도별, 월별 판매량을 시각화
df = pd.DataFrame()
df['Year'] = data['Date'].dt.year
df['Month'] = data['Date'].dt.month
plt.figure(figsize=(10, 10))

ax = df.groupby(['Year', 'Month']).value_counts().plot(kind='bar')#연도별, 월별 판매량 그래프화

for p in ax.patches: #막대 그래프 위에 숫자 표기
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom')

plt.show()

salesman = data['Salesperson'].value_counts().head(5)
print(salesman)

most_sold_car_maker = car_make_counts.idxmax()
print("가장 많이 판 제조사: ", most_sold_car_maker)

most_sold_model = car_model_counts.idxmax()
print("가장 많이 팔린 모델: ", most_sold_model)

year_sale = data.groupby('Car Year')['Sale Price'].sum()
year_sale_perc = year_sale / year_sale.sum() * 100
print(year_sale_perc)

plt.plot(year_sale_perc.index, year_sale_perc.values)
plt.xlabel('Year')
plt.ylabel('Percentage of Sales')
plt.title('Yearly Sales Percentage')
plt.show()

#커미션 분석

plt.figure(figsize=(16, 12))

plt.subplot(321)
data['Commission Rate'].hist(bins=300)
plt.title('commission rate')
plt.subplot(322)
data['Commission Earned'].hist(bins=300)
plt.title('commission earned')
plt.subplot(323)
data['Sale Price'].hist(bins=300)
plt.title("Sale Price")

plt.show()
data['totaltransaction'] = 1 #각 사람의 판매량을 보기 위해 선언
com_piv = pd.pivot_table(data,
                         index= 'Salesperson',
                         aggfunc = {'Sale Price': 'sum', 'Commission Earned': 'sum', 'Commission Rate': 'mean',
                                    'totaltransaction':'sum'})

plt.subplot(221)
x = com_piv['Commission Rate']
y = com_piv['Sale Price']
plt.scatter(x, y, c='Blue')
plt.xlabel('Commission Rate')
plt.ylabel('Sale Price')
plt.show()

plt.subplot(222)
x = com_piv['Commission Earned']
y = com_piv['Sale Price']
plt.scatter(x, y, c='Blue')
plt.xlabel('Commission Earned')
plt.ylabel('Sale Price')
plt.show()

plt.subplot(223)
x = com_piv['Commission Earned']
y = com_piv['totaltransaction']
plt.scatter(x, y, c='Blue')
plt.xlabel('Commission Earned')
plt.ylabel('tataltransaction')
plt.show()

plt.subplot(224)
x = com_piv['Commission Rate']
y = com_piv['totaltransaction']
plt.scatter(x, y, c='Blue')
plt.xlabel('Commission Earned')
plt.ylabel('tataltransaction')
plt.show()