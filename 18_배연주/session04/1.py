# 거스름돈
import sys

change = 1000 - int(sys.stdin.readline())   # 잔돈 = 1000엔 - (물건 가격) 
coins = [500, 100, 50, 10, 5, 1]            # 동전 종류 저장
cnt = 0     # 잔돈의 개수

for coin in coins:              # coins 리스트에서 하나씩 꺼내서
    if change >= coin:          # 잔돈이 coin 보다 크면
        cnt += change//coin     # 동전의 개수는 (잔돈을 coin으로 나눈 몫) 만큼 늘어난다. (Ex. 40원 -> 40 // 10 = 4)
        change %= coin          # coin을 빼낸 값으로 만들어주기

print(cnt)