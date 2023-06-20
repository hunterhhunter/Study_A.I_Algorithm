inp = int(input())      # 테스트 케이스 입력받기

for _ in range(inp):    # 테스트 케이스번 반복
    lis = list(map(int, input().split()))       #공백 기준 값들 리스트로 만들기 -> 먼소린지 모르겠다? -> 디코질문
    n = lis.pop(0)      # pop(0)은 리스트 가장 앞의 원소 제거 -> ?? 난 이게 좀 궁금해 -> 디코 질문
    cnt = 0
    avg = sum(lis) / n  # avr = average 평균입니다.
    for i in lis:   #for-each문 사용 -> 먼소리지?? -> 디코 질문
        if i > avg: #평균 넘는 사람
            cnt += 1
    rate = round((cnt / n) * 100) # 평균 넘는 사람 %구하기 -> 궁금해 -> 디코질문

    print(f"{rate:.3f}%") #포매팅 -> ?? -> 디코 질문