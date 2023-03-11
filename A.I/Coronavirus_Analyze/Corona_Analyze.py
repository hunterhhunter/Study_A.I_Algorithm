import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

corona_all=pd.read_csv("서울시 코로나19 확진자 현황.csv") #데이터 읽어오기
corona_del_col = corona_all.drop(columns=['국적', '환자정보', '조치사항']) #corona_all에서 값이 NaN인 columns 삭제
# dataframe에 추가하기 전, 임시로 데이터를 저장해 둘 list를 선언합니다.
date = []
month = []

for data in corona_del_col['확진일']:
    # split 함수를 사용하여 월, 일을 나누어 list에 저장합니다.
    month.append(data.split('.')[0])
    if len(data.split('.')[1]) == 1:
        date.append('0' + data.split('.')[1])
    else:
        date.append(data.split('.')[1])

# corona_del_col에 `month`, `day` column을 생성하며 동시에 list에 임시 저장된 데이터를 입력합니다.
corona_del_col['month'] = month
corona_del_col['date'] = date

corona_del_col['month'].astype('int64')
corona_del_col['date'].astype('int64')

# 그래프에서 x축의 순서를 정리하기 위하여 order list를 생성합니다.
order = []
for i in range(1, 11):
    order.append(str(i))
'''
# 그래프의 사이즈를 조절합니다.
plt.figure(figsize=(10, 5))

# seaborn의 countplot 함수를 사용하여 출력합니다.
sns.set(style="darkgrid")
ax = sns.countplot(x="month", data=corona_del_col, palette="Set2", order = order)
'''
# 'countplot' 함수를 이용하여 데이터프레임의 값들의 빈도수를 그래프로 출력할 수 있습니다.
# 'x' 파라미터를 통해 데이터프레임에서 x축에 해당하는 열을 지정합니다.
# 'data' 파라미터를 통해 그래프를 그릴 데이터프레임을 지정합니다.
# 'palette' 파라미터를 통해 그래프 색상을 지정할 수 있습니다.
# 'order' 파라미터를 이용하여 데이터프레임에서 x축에 해당하는 열의 값들의 순서를 지정할 수 있습니다.
#plt.show()

# series의 plot 함수를 사용한 출력 방법도 있습니다.
#corona_del_col['month'].value_counts().plot(kind='bar')

# 그래프에서 x축의 순서를 정리하기 위하여 order list를 생성합니다.
order2 = []
for i in range(1, 32):
    order2.append(str(i))
'''
# seaborn의 countplot 함수를 사용하여 출력합니다.
plt.figure(figsize=(20,10))
sns.set(style='darkgrid')
ax = sns.countplot(x="date", data=corona_del_col[corona_del_col['month'] == '8'], palette="rocket_r", order= order2)
plt.show()
'''
'''
퀴즈 1. 8월 평균 일별 확진자 수를 구하세요. (8월 총 확진자/31일)
quiz_1 = len(corona_del_col[corona_del_col['month'] == '8']) / len(corona_del_col.value_counts('date'))
print(quiz_1)
'''
'''
plt.figure(figsize=(20, 10))
plt.rcParams['font.family'] ='Malgun Gothic' #matplotlib에서 한글 보기위해 사용
plt.rcParams['axes.unicode_minus'] =False #
ax = sns.countplot(x="지역", data=corona_del_col, palette="Set2")
plt.show()
'''

# replace 함수를 사용하여 해당 데이터를 변경합니다.
# 이상치가 처리된 데이터이기에 새로운 Dataframe으로 저장합니다.
corona_out_region = corona_del_col.replace({'종랑구':'중랑구', '한국':'기타'})
# plt.figure(figsize=(20, 10))
# plt.rcParams['font.family'] ='Malgun Gothic' #matplotlib에서 한글 보기위해 사용
# plt.rcParams['axes.unicode_minus'] =False #
# ax = sns.countplot(x="지역", data=corona_out_region, palette="Set2")
# plt.show()

# plt.rcParams['font.family'] ='Malgun Gothic' #matplotlib에서 한글 보기위해 사용
# plt.rcParams['axes.unicode_minus'] =False
# plt.figure(figsize=(10, 5))
# sns.set(style="darkgrid")
#관악구 확진자 수가 월별로 증가한 것을 보기위한 그래프
# ax = sns.countplot(x="month", data = corona_out_region[corona_out_region['지역'] == '관악구'], palette="Set2", order = order)
# plt.show()

# 지도 출력을 위한 라이브러리 folium을 import 합니다.
import folium

# Map 함수를 사용하여 지도를 출력합니다.
map_osm = folium.Map(location=[37.529622, 126.984307], zoom_start=11)

CRS = pd.read_csv("서울시 행정구역 시군구 정보 (좌표계_ WGS1984).csv")

# corona_out_region의 지역에는 'oo구' 이외로 `타시도`, `기타`에 해당되는 데이터가 존재 합니다.
# 위 데이터에 해당되는 위도, 경도를 찾을 수 없기에 삭제하여 corona_seoul로 저장합니다.
corona_seoul = corona_out_region.drop(corona_out_region[corona_out_region['지역'] == '타시도'].index)
corona_seoul = corona_seoul.drop(corona_out_region[corona_out_region['지역'] == '기타'].index)

# 서울 중심지 중구를 가운데 좌표로 잡아 지도를 출력합니다.
map_osm = folium.Map(location=[37.557945, 126.99419], zoom_start=11)
# 지역 정보를 set 함수를 사용하여 25개 고유의 지역을 뽑아냅니다.
for region in set(corona_seoul['지역']):
    # 해당 지역의 데이터 개수를 count에 저장합니다.
    count = len(corona_seoul[corona_seoul['지역'] == region])
    # 해당 지역의 데이터를 CRS에서 뽑아냅니다.
    CRS_region = CRS[CRS['시군구명_한글'] == region]
    # CircleMarker를 사용하여 지역마다 원형마커를 생성합니다.
    marker = folium.CircleMarker([CRS_region['위도'], CRS_region['경도']],
                                 radius=count/10 + 10,
                                 color='#3186cc',
                                 fill_color='#3183cc',
                                 popup=' '.join((region, str(count), '명')))
    marker.add_to(map_osm)

map_osm.show_in_browser()