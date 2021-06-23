num = int(input("숫자를 입력하세요 >> "))
fac = 1
print(num,'!=',end='')

for i in range(num, 0, -1):
    fac *= i
    if (i != 1):
        print(i,'x',end='')
    else:
        print(i,'=',fac)