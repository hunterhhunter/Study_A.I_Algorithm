# def reculsive(i):
#     if i == 100:
#         return
#     print(i, "째 재귀에서 ", i+1, '번째 재귀호출')
#     reculsive(i+1)
#     print(i, '번째 재귀함수 종료')
#
# reculsive(1)

# def fectorial_iterrative(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result
# def fectorial_reculsive(n):
#     if n <= 1:
#         return 1
#     return n * fectorial_reculsive(n-1)
# print('반복구현', fectorial_iterrative(5))
# print('재귀구현', fectorial_reculsive(5))

def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)
print(GCD(192, 162))