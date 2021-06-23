quizResult = input("OX퀴즈의 결과를 입력하세요 >> ")
# 연속 점수
inARow = 1 
# 총 점수 
point = 0

print("\n\"" + quizResult + "\"의 점수는 ", end="")
# 점수 계산 및 과정 출력 반복문
for result in quizResult:
    if result=="O" or result=="o":      # 정답일 경우
        print(str(inARow) +" + ", end="")
        point += inARow                 # 총 점수 + 연속 점수
        inARow += 1                     # 연속 점수 ++
    elif result=="X" or result=="x":    # 틀렸을 경우
        print("0 + ", end="")
        inARow = 1                      # 연속 점수 1점으로 초기화

# 결과 출력
print("\b\b= "+str(point) + "점입니다.\n")