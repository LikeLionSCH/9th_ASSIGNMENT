userInput = int(input("숫자를 입력하세요 >> "))

if userInput % 2 == 0:
    print(str(userInput) + ("은(는) 짝수입니다."))
else:
    print(str(userInput) + ("은(는) 홀수입니다."))