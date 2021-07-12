product_price = [1000, 5000, 7500, 10000, 2500, 3000, 4500, 6000]
for i in range(8):
    print('{}번째 상품 가격: {}'.format(i, product_price[i]))

i = 0
buy = 0

money = int(input("가지고 있는 돈을 입력하세요 >> "))

for i in product_price:
    money = money - i
    if money < 0:
        break
    elif money >= 0:
        buy += 1

print("돈이 모자랍니다.", buy, "개의 상품을 샀습니다.")
    