num = int(input())
distance = list(map(int, input().split()))
price = dict()
lis = list(map(int, input().split()))

for i in range(num):
    price[i] = lis[i]
mid_dis, mid_price, result = 0, price[0], 0

for i in range(num-1):
    mid_dis += distance[i]
    if mid_price > price[i+1]:
        result += mid_price * mid_dis
        mid_dis, mid_price = 0, price[i+1]

result += mid_price * mid_dis
print(result)