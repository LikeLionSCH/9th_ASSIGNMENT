change = 1000-int(input())   # 거스름돈
coins = [500, 100, 50, 10, 5, 1]    # 동전 종류
coinCount = 0   # 동전 개수

# 동전 개수 계산
for coin in coins:
    if change >= coin:
        coinCount += change//coin
        change %= coin

# 동전 개수 출력
print(coinCount)