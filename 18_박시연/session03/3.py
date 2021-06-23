list = [1000, 5000, 7500, 10000, 2500, 3000, 4500, 6000]
print("0번째 상품 가격 : ", list[0])
print("1번째 상품 가격 : ", list[1])
print("2번째 상품 가격 : ", list[2])
print("3번째 상품 가격 : ", list[3])
print("4번째 상품 가격 : ", list[4])
print("5번째 상품 가격 : ", list[5])
print("6번째 상품 가격 : ", list[6])
print("7번째 상품 가격 : ", list[7])
n=0

money = int(input("가지고 있는 돈을 입력하세요 >> "))

while((n < 8)):
    money = money - list[n]

    if (money < 0):
        print("돈이 모자랍니다.", end=" ")
        break

    n = n+1

print(n, "개의 상품을 샀습니다.")