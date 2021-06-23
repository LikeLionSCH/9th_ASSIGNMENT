money = int(input())
change = 1000-money
coinCount = change//500 #몫
changed = change%500 #나머지
coin = 500
countC = 1
while 1 :
    if countC == 0 :
        coin = coin//2
        if coin == 0:
            break
        coinCount = coinCount + changed//coin
        changed = changed%coin
        countC = 1
    elif countC == 1 :
        coin = coin//5
        if coin == 0:
            break
        coinCount = coinCount + changed//coin
        changed = changed%coin
        countC = 0
print(coinCount)
    
        
