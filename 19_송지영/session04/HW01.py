charge = 1000 - int(input("얼마 짜리를 샀나요?"))

s = [500, 100, 50, 10 ,5, 1] #동전 가치 저장 리스트

num = 0 #동전개수 저장 변수
i = 0 #s의 인덱스 변수

while charge != 0 : #남은 거스름돈이 0이 될 때까지
    num += charge // s[i] 
    charge %= s[i]
    i += 1

print(num)