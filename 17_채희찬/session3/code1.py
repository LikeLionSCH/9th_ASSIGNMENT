userInput = int(input("숫자를 입력하세요 >> "))
sumNumber = 1

print(str(userInput) + "! = ", end="")

for count in reversed(range(1, userInput+1)):
    print(str(count) + "x", end="")
    sumNumber = sumNumber * count

print("\b = " + str(sumNumber))