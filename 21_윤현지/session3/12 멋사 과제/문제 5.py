#O이 연속되면 연속된 횟수만큼 점수가 부여됨 ex) OXXXXOO=1+0+0+0+0+1+2=4점

result=input("퀴즈 결과를 O, X로 입력해 주세요: ") #퀴즈 결과 입력 받기

score=0 #score 초깃값
sum=0 #sum의 초깃값

for i in result:
    if(i=='O'): #O일 때에는
        sum=sum+1 #1점 추가
        score+=sum #O가 연속으로 나오면 값 증가
    elif(i=='X'): #X일 때에는
        sum=0 #score 0점

print(score,"점 입니다.")