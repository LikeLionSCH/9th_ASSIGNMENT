list = [1000,5000,7500,10000,2500,3000,4500,6000]
# print("0번째 상품 가격:",list[0])
# print("1번째 상품 가격:",list[1])
# print("2번째 상품 가격:",list[2])
# print("3번째 상품 가격:",list[3])
# print("4번째 상품 가격:",list[4])
# print("5번째 상품 가격:",list[5])
# print("6번째 상품 가격:",list[6])
# print("7번째 상품 가격:",list[7])

for i in range(8):
    print(i,"번째 상품 가격:",list[i])

money = int(input("가지고 있는 돈을 입력하세요 >> "))
sum = 0
num = 0
for i in list:
    sum += i
    num += 1
    if(sum>money):
        break
print('돈이 모자랍니다.',num-1,'개의 상품을 샀습니다.')