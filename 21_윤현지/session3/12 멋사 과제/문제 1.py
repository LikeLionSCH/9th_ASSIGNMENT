num=int(input("숫자를 입력하세요: "))
factorial = 1
for i in  range(1,num+1):
    factorial *=i

print(i,"!=",factorial)