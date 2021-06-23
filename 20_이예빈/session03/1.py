# 사용자로부터 숫자 n을 입력받아 n! 을 출력하는 프로그램을 작성하라

n = int(input("숫자를 입력하세요 >> "))
result=1
print(f"{n} ! = ", end='')

while (True):
    print(f"{n}", end='')
    result*=n
    n-=1
    if(n==0):
        break
    print("x", end='')
print(f" = {result}")
