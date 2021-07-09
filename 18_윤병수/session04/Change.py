Money = int(input("지불해야 하는 돈은 얼마인가요? => "))

change = 1000 - Money

change_money = [500, 100, 50, 10 ,5, 1]
count = 0

for i in range(6) :
    if change >= change_money[i] :
        change -= change_money[i]
        count = count + 1

print("최소한의 잔돈 개수는" + count + "입니다.")