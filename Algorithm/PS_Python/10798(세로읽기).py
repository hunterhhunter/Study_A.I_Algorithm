words = []
length = []
for _ in range(5):
    word = input()
    words.append(word) #문자열 리스트에 넣기
    length.append(len(word)) #길이도 넣어주기

rst = ''
for i in range(max(length)): #제일 긴 친구만큼 반복할거임 -> 출력 못 하면 안되니가
    for j in range(5): # 문자열 5개 들어오는거 확정
        if i < length[j]: #지금 j번째 문자열의 길이는 어느정도야? -> j번째 문자열 넘었어? -> 하지마 그럼
            rst += words[j][i] #문자열 연산

print(rst)