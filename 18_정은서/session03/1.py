factorial = int(input("숫자를 입력하세요 >>"))
fac = 1
for n in range(factorial):
    fac *= n+1

print(fac)