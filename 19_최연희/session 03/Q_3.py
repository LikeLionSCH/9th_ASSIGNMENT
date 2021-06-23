sum = 0
count = 0
price=[1000,5000,7500,10000,2500,3000,4500,6000]
for i in range(8):
    print(i,"번째 상품 가격:",price[i])

money = int(input("가지고 있는 돈을 입력하세요 >> "))

for i in range(8):
    sum += price[i]
    if (sum < money):
        count += 1
    else:
        break
print("돈이 모자랍니다. ",count,"개의 상품을 샀습니다.")

