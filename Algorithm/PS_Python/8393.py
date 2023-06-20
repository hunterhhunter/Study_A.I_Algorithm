num = int(input()) #입력받기

print(int((num * (num + 1))/2)) # ?? 뭐임? 1~n까지 더하라며
# -> 1~n까지 모두 더한 값은 n*(n+1)/2 식과 같은 값이다. -> 시그마 공식

# # 2번 풀이
# hap = 0
# for i in range(1, num+1):
#     hap += i
# print(hap)
# # 3번 풀이
# for i in range(num):
#     hap += i+1
# print(hap)
#
# # 4번 풀이 (while문)
# i = 0
# while i<10:
#     hap += i+1
#     i += 1
# print(hap)
