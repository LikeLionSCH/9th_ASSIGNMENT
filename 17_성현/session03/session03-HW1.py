print("숫자를 입력하세요 >>", end=' ') 
num1 = int(input()) 
sum = 1 
print(num1,'! =', end=' ')
while(True) :
    sum*=num1
    print(num1, end=' ')
    if num1>0 :
        print('x', end=' ')
        num1 -=1
    if num1==0 :
        print('=',sum)
        break