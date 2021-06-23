merchandise = [1000, 5000, 7500, 10000, 2500, 3000, 4500, 6000]
for index, price in enumerate(merchandise):
    print(str(index) + "번째 상품 가격 : " + str(price))

pay = int(input("가지고 있는 돈을 입력하세요 >> "))

for index, price in enumerate(merchandise):
    if price > pay:
        print("돈이 모자랍니다. " + str(index) +"개의 상품을 샀습니다.")
        exit()
    pay = pay - price

print("모든 상품을 모두 샀습니다.")