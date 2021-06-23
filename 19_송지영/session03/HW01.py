n = int(input("숫자를 입력하세요 >> "))

def factorial(n):
    if n == 1:  
        return 1    
    return n * factorial(n - 1)    

print(str(n)+"! = ", end='')

for i in range(n, 0 , -1):
    if(i > 1):
        print(str(i) + "x", end= '')
    elif(i == 1):
        print("1 = ", end="")

print(factorial(n))