put=int(input("상품은 얼마일까요?: "))
exchange = 1000-put
coin=0
coinlist = [500,100,50,10,5,1]

for c in coinlist:
    coin += exchange//c
    exchange%=c

print(coin)