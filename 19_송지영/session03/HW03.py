items = [1000, 5000, 7500, 10000, 2500, 3000, 4500, 6000]

n = 0
for i in items:
    print(str(n)+"번째 상품 가격:",i)
    n = n+1

money = int(input("가지고 있는 돈을 입력하세요 >> "))

sum = 0
for x in range(0, 7):
    sum += items[x]

if(sum > money):
    print("돈이 모자랍니다.", x , "개의 상품을 샀습니다.")
