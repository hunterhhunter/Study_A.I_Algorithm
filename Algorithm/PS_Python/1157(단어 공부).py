#제 1풀이

inp = input().upper() #대소문자 구분 안하고 개수를 센다고 해서 upper로 대문자 변환
lis = [0 for _ in range(26)] #알파벳 개수만금 0이 담긴 리스트 선언
al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #알파벳 A-Z

for i in range(len(al)): #알파벳 리스트 for 구문으로 돌면서 몇개 들어있는지 개수 세기
    lis[i] = inp.count(al[i]) #카운트 함수 사용

if lis.count(max(lis)) > 1: #많이 쓰인 수가 2개 이상일 경우
    print('?')
else:
    print(al[lis.index(max(lis))]) #가장 큰 값의 인덱스를 얻어 알파벳 문자열에 접근


# 제 2풀이
inp = input().upper()
inp_list = list(set(inp)) #집합 자료형으로 중복 제거

cnt = []

for i in inp_list:
    lis.append(inp.count(i))

if cnt.count(max(cnt)) > 1: #많이 쓰인 수가 2개 이상일 경우
    print("?")
else:
    print(inp_list[(cnt.index(max(cnt)))])
#전과 마찬가지로 가장 많이 쓰인 값의 인덱스를 얻어 알파벳이 담긴 리스트에 접근