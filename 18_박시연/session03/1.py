n = int(input("숫자를 입력하세요 >> "))
result = n

print(n, "! = ", n, end=" ")

while (n > 1):
    n = n-1
    print("×", n, end=" ")
    result = result * n

print(" = ", result)
