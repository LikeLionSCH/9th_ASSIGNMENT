#거스름돈

price = int(input())
change = 1000 - price       #잔돈 계산

coins = [500, 100, 50, 10, 5, 1] 

count = 0                    #잔돈 개수 입력할 변수 선언

for i in coins:              #coins 리스트 만큼 반복
    count += change // i     #count에 change를 coins로 나눈 몫을 누적 입력
    change %= i              #change를 coins로 나눈 나머지값을 다시 change에 입력
print(count)

