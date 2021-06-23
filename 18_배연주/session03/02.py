# 사용자로부터 숫자 한 개를 입력받아 그 수가 홀수인지 짝수인지 출력하는 프로그램을 작성하라.
n = int(input())

if n % 2 == 0:
    print("{}은 짝수입니다.".format(n))
else:
    print("{}은 홀수입니다.".format(n))