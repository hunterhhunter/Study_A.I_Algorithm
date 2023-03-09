#문제 : 2개씩 연속되어 입력된 숫자들을 하나로 줄인 후 그 수를 이진수로 출력

string_num = input()

a = list(string_num)  # 2번씩 써지는 부분을 1번만 써지게 수정
for i in range(len(a) - 1):

    if a[i] == a[i + 1]:  # a[i] 가 다음 원소와 같으면 다음 원소를 공백으로 초기화
        a[i + 1] = ''
z = ''.join(a)  # 리스트를 다시 합친다.

c = []

def ee(n):  # 2진수로 바꿔주는 함수
    while n != 1:  # 1이 될때까지 실행
        if n % 2 == 0:  # 짝수일 경우
            c.append('0')  # c리스트에 0 추가
            n = n // 2  # 2로 나누기
        else:  # 짝수일 경우
            c.append('1')  # 1추가
            n = n // 2
    c.append('1')  # 마지막에 1 추가시키기
    c.reverse()  # 2진수로 나타내기위해 reverse()
    return ''.join(c)  # 합쳐진 c를 반환


print(ee(int(z)))
print("HelloWorld")