round = int(input("몇 라운드? >> "))
#전체 몇 번 반복할 지 입력 받기

score = 0 
final = 0
# 함수 선언

for i in range(0, round):
    # round에 입력 받은 수 만큼 반복
    result = input("퀴즈 결과를 입력하세요 >> ")
    # 퀴즈 결과 입력 받기
    for j in result:
        # 입력 받은 문자열 반복
        if j == 'O' :
            # 문자가 "O"면 score에 1씩 더하기
            score += 1
            # 누적해서 더하기
        else :
            # 문자가 "O"가 아니면 score 0으로 초기화
            score = 0
        final += score
        # j문자열 반복할 때 마다 final에 score 누적해서 더하기
    print(final)
    final = 0