goal_price = int(input()) #목표금액
count = int(input()) #상품 몇 개 샀어?
all_price = 0 #총가격

for i in range(0, count): #반복
    price, quantity = map(int, input().split()) #다중입력
    all_price += price * quantity #총 가격에 비용과 양을 곱한 가격을 더해주기

if goal_price == all_price: #총 가격과 목표가격이 같으면?
    print("Yes") #예스!!
else: #아니면?
    print("No") #노!