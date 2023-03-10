import pandas as pd
import numpy as np
'''
df = pd.DataFrame(
        np.arange(0, 25).reshape(5, 5),
        index=['밥', '집', '치킨', '방', '내'],
        columns=['치', '즈', '김', '키', '전']
)
print(df)
print(df.iloc[2, 1])
print(df.loc['방', '키'])
print(df.loc['집':, "김"])
'''
'''
import seaborn as sns
titanic = sns.load_dataset("titanic")
titanic.head()

print(titanic)
print(titanic['age'].mean())
print(titanic.loc[titanic.sex == "female"]["age"].mean())
print(titanic.loc[(titanic['pclass'] == 1) & (titanic['sex'] == "female")]["age"].mean())
'''

import seaborn as sns
titanic = sns.load_dataset("titanic")
titanic.head()
titanic["adult/child"] = titanic.apply(lambda r: "adult" if r.age >= 20 else "child", axis=1)
#adult와 child를 나누는 열을 추가하는 줄 lambda 에서 r이 20살이 넘으면 adult로 삽입 아니면 어린이
titanic.tail()

titanic["category1"] = titanic.apply(lambda z: z.sex if z.age >= 20 else "child", axis=1)
#20살이 넘으면 성별 아니면 child를 입력하는 줄

titanic.fillna({'age': round(float(titanic.age.mean()), 0)}, inplace=True)
# 비어있는 나이에 평균 나이를 입력하는 줄 round는 반올림 round(숫자, 소수점) inplace = True of False 저장할거면 True

titanic["category2"] = titanic.sex + titanic.age.astype(str)
#성별과 나이를 합치는 category2를 만드는 줄

bins = [0, 20, 30, 50, 70, 100]
labels = ["미성년자", "청년", "중년", "장년", "노년"]
titanic["연령대"] = pd.cut(titanic.age, bins, labels=labels) # 연령대 카테고리 추가
titanic["a"] = pd.cut(titanic.age, bins, labels=labels)

titanic_age = pd.DataFrame(titanic.연령대.value_counts(), columns=["연령대"]) # 연령대 데이터프레임
titanic_age["비율"] = titanic_age.apply(lambda i : i.연령대 / titanic_age.연령대.sum(), axis=1) #비율 카테고리
# print(titanic_age)
#
# print([i for i in titanic['age'] if (i * 10) % 10 != 0]) # 소수점이 있는 나이들을 출력
# print(a.value_counts() / sum(a.value_counts()))
# 나이 그룹의 승객 비율을 구하는 식

titanic['category3'] = titanic.apply(lambda f: "미성년자" if f.age < 20 else f.a + f.sex, axis=1)
print(titanic)
'''


print(sum(a.value_counts()))
 '''

#print(titanic)

'''
df3 = pd.DataFrame({
    'A': [1, 3, 4, 3, 4],
    'B': [2, 3, 1, 2, 3],
    'C': [1, 5, 2, 4, 4]
})
print(df3.apply(lambda x: x.max() - x.min())) #각 열의 최댓값과 최솟값을 구하고 싶을 때
'''
'''
ages = [0, 2, 10, 21, 23, 37, 31, 61, 20, 41, 32, 101]
bins = [1, 20, 30, 50, 70, 100]
labels = ["미성년자", "청년", "중년", "장년", "노년"]
cats = pd.cut(ages, bins, labels=labels)
print(cats)

df4 = pd.DataFrame(ages, columns=["ages"])
df4["age_cat"] = pd.cut(df4.ages, bins, labels=labels)
print(df4.age_cat.astype(str) + df4.ages.astype(str))
'''
