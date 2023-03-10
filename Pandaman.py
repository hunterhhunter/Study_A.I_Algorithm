import pandas as pd
import numpy as np
import csv
'''s1 = pd.Series(range(0, 5), index=["야", "반", "가", "워", "이"])
s2 = pd.Series(range(3, 8), index=["야", "반", "갑", "워", "이"])

print(s1 + s2)
print(s2 - s1)
print(s1 * s2)
print(s2 / s1)
'''

'''data = {
    "2015": [9904312, 3448737, 2890451, 2466052],
    "2010": [9631482, 3393191, 2632035, 2431774],
    "2005": [9762546, 3512547, 2517680, 2456016],
    "2000": [9853972, 3655437, 2466338, 2473990],
    "지역": ["수도권", "경상권", "수도권", "경상권"],
    "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]
}
columns = ["지역", "2015", "2010", "2005", "2000", "2010-2015 증가율"]
index = ["서울", "부산", "인천", "대구"]
DF = pd.DataFrame(data, index= index, columns= columns)
print(DF)
DF.index.name = "도시"
DF.columns.name = "특성"
print(DF)'''

'''im = {
    "집": [1, 2, 3, 4, 5],
    "home":["아", "가", "고", "싶", "다"],
    "par":[0.1, 0.2, 0.3, 0.4, 0.5],
    "so":[123, 124, 144, 535, 566],
    "SS":[11.2, 33.5, 42.4, 23.5, 23.6]
}

columns = ["집", "home", "par", "so", "SS"]
index = ["내가", "생각", "나는", "것들", "적음"]
DF = pd.DataFrame(im, index=index, columns=columns)
print(DF.index, DF.columns)
DF.index.name = "하이"
DF.columns.name = "야임마"
print(DF)
print(np.transpose(DF))'''

'''data = {
    "국어": [80, 90, 70, 30],
    "영어": [90, 70, 60, 40],
    "수학": [90, 60, 80, 70],
}
columns = ["국어", "영어", "수학"]
index = ["춘향", "몽룡", "향단", "방자"]
df = pd.DataFrame(data, index=index, columns=columns)
print(data["수학"])
print(df[['국어', '영어']])
df["평균"] = df.mean(axis=1)
print(df)
df.loc["방자", "영어"] = 80
df["평균"] = df.mean(axis=1)
print(df)
print(df[:1])
print(pd.Series((list(df[2:3].values)), index=["향단"]))
'''
'''
def gipgap(year, size, num):
    return year * size * num


wich_num = {'서울':5, '부산':4, '광주':1, '울산':3, '광명':2}
wich_ordered = sorted(wich_num, key=wich_num.get)
pyong = [15, 20, 25]
nal = [2010, 2015, 2020, 2022]
df = pd.DataFrame(index= nal, columns=pd.MultiIndex.from_product([wich_num.keys(), pyong]))
df.index.name = '연도'
df.columns.names = ['위치', '평수']

for z in wich_num:
    for i in nal:
        for x in pyong:
            num = wich_num[z]
            df.loc[i, (z, x)] = gipgap(i, x, num)


print(df)'''