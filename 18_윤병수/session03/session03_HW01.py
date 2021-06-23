num = int(input("숫자를 입력하세요 >> "))
num1 = 1
calcul_list = []

for i in range(1, num+1):
    if num == 0:
        print(num + "!" + " = " + "1")
    else:
        num1 *= i
        i = i - 1

while i >= 0:
    calcul_list.append(i+1)
    i = i - 1

print(num,"!"," = ",calcul_list, " = ", num1)
