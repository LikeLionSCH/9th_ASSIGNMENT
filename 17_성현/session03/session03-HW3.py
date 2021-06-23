manuf = [1000,5000,7500,10000,2500,3000,4500,6000]
for num in range(len(manuf)) :
    print(num,'번째 상품 가격: ',num)
print('가지고 있는 돈을 입력하세요 >>', end=' ')
money = int(input()) 
sum = 0
for num in range(len(manuf)) :
    sum +=manuf[num]
    if sum>money :
        print('돈이 모자랍니다.',num,'개의 상품을 샀습니다.')
        break
    elif sum==money :
        print('돈이 딱 맞습니다. 알뜰하게 샀습니다.')
    elif sum<money and num==7 :
        print('돈이 남습니다. 모든 상품을 샀습니다.')