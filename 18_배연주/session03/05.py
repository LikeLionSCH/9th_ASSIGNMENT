# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.
# 예를 들어 10번 문제의 점수는 3이 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3=10점이다.
# OX 퀴즈의 결과가 주어졌을 떄, 점수를 구하는 프로그램을 작성하시오.
n = int(input())    # 테스트 케이스의 개수


for i in range(n):  # 테스트 케이스만큼 반복
    score = 0
    count = 0       # 연속된 O의 개수를 카운트할 변수
    a = input()

    for j in a:
        if j == 'O':            # 'O'인 경우
            count += 1          # 'O'가 나왔으니 count + 1
            score += count      # count 만큼 더해주기
        elif j == 'X':          # 'X'인 경우
            count = 0           # count 0로 초기화

    print(score)