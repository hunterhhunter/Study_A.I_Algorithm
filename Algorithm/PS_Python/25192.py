import sys
input = sys.stdin.readline
inp = int(input())
lis = set()
count = 0
for i in range(inp):
    a = input()
    if a == 'ENTER\n':
        lis = set()
    else:
        if a not in lis:
            count += 1
            lis.add(a)
print(count)

def gomgomi(n):
    gomgom = set()
    cnt = 0
    for _ in range(n):
        word = input()

        # ENTER가 아니고, 새로 접속한 사람이 아니면 횟수 증가
        if word != 'ENTER':
            if word not in gomgom:
                cnt += 1
                gomgom.add(word)
        # ENTER이면, 기존에 접속한 회원 정보 초기화
        elif word == 'ENTER':
            gomgom.clear()

    return cnt


print(gomgomi(int(input())))