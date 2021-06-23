n = int(input("숫자를 입력하세요 >> "))

if(n == 0):
    print("0은 홀짝을 따질 수 없습니다.")
elif(n%2 == 0):
    print(n, "은 짝수입니다.")
elif(n%2 == 1):
    print(n, "은 홀수입니다.")
else:
    print("입력하기 전에 생각했나요?")