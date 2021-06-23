# 연속된 O의 개수만큼 점수 부여됨

# result="OOXXOXXOOO" (1+2)+(1)+(1+2+3)==10점
result=input("OX퀴즈의 결과 입력 >> ") # 사용자에게 OX에 대한 문자열 입력받음
sum=0 # sum 초깃값 (점수의 총합)
cnt=0 # cnt 초깃값 (연속된 O의 개수에 따라 증가)

for i in result:
    if(i=='O'): # O 라면
        cnt+=1 # O가 연속으로 나올 때 마다 cnt값 증가
        sum+=cnt # sum에 cnt 대입
    else: # X 라면 cnt를 0으로 초기화
        cnt=0

print(f"총점은 {sum}")