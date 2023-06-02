def fibonacci(num):
    for i in range(3, num+1):
        fibo.append(fibo[i] + fibo[i-1])

i = int(input())

for x in range(i):
    fibo = [0, 1, 1, 2]
    a = int(input())
    if a == 0:
        print(1, 0)
    else:
        fibonacci(a)
        print(fibo[a-1], fibo[a])

#도현이형 풀이
zero, one = 0, 0
fibonacci_list = [[1, 0], [0, 1], [1, 1]]
def dp_fibonacci(num):
    for i in range(3, num+1):
        a, b = fibonacci_list[-1]
        fibonacci_list.append([b, a+b])
    print(f"{fibonacci_list[num][0]} {fibonacci_list[num][1]}")

testcase = int(input())

for test in range(testcase):
    test = int(input())
    dp_fibonacci(test)