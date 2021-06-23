# 사용자에게 케이스의 개수를 입력받는다.
num = int(input())

# 입력받은 개수만큼 반복문을 실행한다.
for i in range(num):

    # 사용자에게 OX퀴즈 결과를 입력받는다.
    case = str(input())

    # score와 count의 값을 초기화해준다.
    score = 0
    count = 0

    # 점수를 계산하기 위한 반복문을 실행한다.
    for j in list(case):

        # O일 경우에 1점을 더해준다.
        if j == "O":
            count += 1
            # 전체 점수에 점수를 합해준다.
            score += count

        # X일경우,
        elif j == "X":            
            count = 0 # 0점을 더해준다.
    print(score) # 전체 점수 출력해준다.