inp = int(input())
time = list(map(int, input().split()))
f_time, tmp = 0, 0
time.sort()
for i in time:
    f_time += i + tmp
    tmp += i
print(f_time)

import sys
n = int(sys.stdin.readline())
time = list(map(int,sys.stdin.readline().split()))
time.sort()
sum = 0
for i in range(n):
    sum += time.pop() * (i+1)
print(sum)

min_sum  = 0

N = int(input())
data_list = list(map(int, input().split()))

data_list.sort()

for i in range(N):
    min_sum += data_list[i] * (N - i)

print(min_sum)