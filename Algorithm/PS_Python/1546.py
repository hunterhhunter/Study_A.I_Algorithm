count_of_subject = int(input()) #과목 개수
lis = list(map(int, input().split()))

max_num = max(lis) #최댓값 찾기
sum_of_score = sum(lis) #기존 점수의 총합
average = (sum_of_score / count_of_subject) / max_num * 100
#새로운 평균을 구해볼 것이다.
#각 점수들에 새로운 점수 체계를 적용해 평균을 구하는 것이 문제다.
#이 때 .... 말로 설명 못하겠습니다.
#궁금하시면 조영진에게로...
#각 점수에 식을 적용하고 평균을 구하나 평균에 식을 적용하는 거나 다를게 없다는게 내 말인데....
print(average)
