n = int(input("테스트 개수를 입력하세요 ")) #테스트 개수 입력 받기
score = 0   
Total_score = 0

for i in range(n): #테스트 개수 만큼 for문 돌기
    a = list(input("퀴즈 결과를 입력하세요 "))   #퀴즈 결과값 입력
    for j in a: #a 개수 만큼 돌기 
        if (j == 'O'): #r이 'O'일때
            score = score +1    #연속하는 'O'의 개수만큼 1더하여 계산하고,
            Total_score = Total_score + score #Total_score에 score만큼 더한다.
        elif (j == 'X') :  #r이 'X'이면
            score = 0   # score점수는 0

    print(Total_score)
    #다음 입력을 위해 score와 Total_score 초기화
    score = 0
    Total_score = 0