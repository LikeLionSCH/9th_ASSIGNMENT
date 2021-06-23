exchange = 1000-int(input())
coin = [500,100,50,10,5,1]
answer = 0

for i in coin:
   answer += exchange // i
   exchange %= i

print(answer)