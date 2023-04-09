goal_price = int(input())
count = int(input())
all_price = 0

for i in range(0, count):
    price, quantity = map(int, input().split())
    all_price += price * quantity

if goal_price == all_price:
    print("Yes")
else:
    print("No")