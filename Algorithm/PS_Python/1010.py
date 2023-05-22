inp = int(input())

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

for _ in range(inp):
    a, b = map(int, input().split())
    print(factorial(b) // (factorial(a) * factorial(b-a)))