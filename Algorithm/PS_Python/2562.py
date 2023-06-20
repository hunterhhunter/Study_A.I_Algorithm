lis = [int(input()) for _ in range(9)] #리스트 컴프리헨션 -> ?? -> 길게 쓰기 싫어서 쓰는 짧은 표현
# 위의 문장을 해제해서 적어보자
# lis = []
# for i in range(9):
#     num = int(input())
#     lis.append(num)

# -> ?? 4줄을 1한줄로?
print(max(lis)) # 최댓값 찾기
print(lis.index(max(lis))+1)
# 숫자의 인덱스 위치 찾기 .index(숫자) 인덱스 위치 찾아줌
# -> 인덱스는 0부터 시작 -> +1 해줌