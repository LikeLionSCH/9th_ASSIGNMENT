import math
n = int(input("숫자를 입력하세요 >> "))
hap = 1

print(str(n)+"! =", end=" ")

for i in range (n, 0, -1) :
    hap = hap * i
    if i == 1:
        print(i, end="")
    else :
        print(i, end="x")

print(" =", hap)

# result = (math.factorial(n))
# print(n, "! =", result)

