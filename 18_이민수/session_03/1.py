n = int(input("숫자를 입력하세요 >> "))

def factorial(n):
    if n == 0:  
        return 1    
    return factorial(n - 1)*n    

print(factorial(n)) 