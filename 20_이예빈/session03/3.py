list=[] # 빈 리스트 생성
sum=0 # 총합 sum 초깃값

for i in range(7): # 총 7개의 상품에 대한 가격 입력 받음
    print(i, end="")
    n=int(input("번째 상품 가격: "))
    sum+=n # 입력 받은 가격을 sum에 저장
    list.append(n) # 리스트의 끝에 요소 n값을 추가
print(list)

# 전체 상품 구매 불가능한 경우
price=int(input("가지고 있는 돈을 입력하세요 >> "))
if price<sum:
    print("돈이 모자랍니다. ", end="")

i=0
while(True):
    price-=list[i] # 리스트의 첫번째 요소부터 price값에서 차례대로 뻄
    if(price<0): # price가 0보다 작아지면 반복문 빠져나감
        break
    i+=1
print(f"{i}개의 상품을 샀습니다.")