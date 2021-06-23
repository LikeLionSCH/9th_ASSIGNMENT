item_price = [1000, 5000, 7500, 10000, 2500, 3000, 4500, 6000]
i = 0

print("0번째 상품 가격: 1000")
print("1번째 상품 가격: 5000")
print("2번째 상품 가격: 7500")
print("3번째 상품 가격: 10000")
print("4번째 상품 가격: 2500")
print("5번째 상품 가격: 3000")
print("6번째 상품 가격: 4500")
print("7번째 상품 가격: 6000")

mm = int(input("가지고 있는 돈을 입력하세요 >> "))
# mm == My_Money
cnt = 0
for i in item_price:
    mm -= i
    if mm < 0:
        print("구매해주셔서 정말 감사합니다.")
        break
    elif mm >= 0:
        cnt += 1
print("돈이 모자랍니다.", cnt, "개의 상품을 샀습니다.")
    
    
        
    
