# 가게에 상품이 진열되어 있습니다.
# 가지고 있는 돈을 입력했을 때 그 돈으로 얼마나 살 수 있는지 출력하는 프로그램을 작성하세요.
# 단, 효율을 무시하고 예시와 같게 만들어야 합니다.
price = [1000, 5000, 7500, 10000, 2500, 3000, 4500, 6000]
for i in range(8):
    print('{}번째 상품 가격: {}'.format(i, price[i]))


money = int(input('가지고 있는 돈을 입력하세요 >> '))
result = price[0]
cnt = 0
for i in range(8):        
    result += price[i]
    if result <= money:
        cnt += 1
    else:
        print('돈이 모자랍니다. {}개의 상품을 샀습니다.'.format(cnt))
        break

