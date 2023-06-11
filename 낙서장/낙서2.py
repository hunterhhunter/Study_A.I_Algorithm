# 다음과 같이 import를 사용할 수 있습니다.
# import math
from collections import deque


def solution(garden):
    lis = garden
    # 여기에 코드를 작성해주세요.
    q = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(len(lis)):
        for z in range(len(lis[0])):
            if lis[i][z] == 1:
                q.append([i, z])

    while q:
        x, y = q.popleft()


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= len(lis) or ny >= len(lis[1]) or nx < 0 or ny < 0:
                continue
            if lis[nx][ny] != 0:
                continue

            lis[nx][ny] = lis[x][y] + 1
            q.append([nx, ny])
    answer = 0
    for r in lis:
        answer = max(answer, *r)
    return answer-1


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0],[0, 0, 0], [0, 1, 0], [0, 0, 0],[0, 0, 0], [0, 1, 0], [0, 0, 0],[0, 0, 0], [0, 1, 0], [0, 0, 0],[0, 0, 0], [0, 1, 0], [0, 0, 0],[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(garden1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

garden2 = [[1, 1], [1, 1]]
ret2 = solution(garden2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")