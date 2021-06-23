'''
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX
'''

problem = {}        #문제가 들어갈 list
problemst = 0       #연속으로 문제를 맞췄는가? 맞췄으면 1, 못맞췄으면 0. 초기값은 0
correctnum = 0      #문제의 점수를 계산한 횟수 = 점수 계산한 list 인덱스
plusscore = 2       #만약 연속으로 문제를 맞췄을 시 획득하는 추가 점수. 기본적으로 받는 1점을 포함하여 +1이기 떄문에 초기값이 2가 된다.
score = 0           #사용자가 획득하게 되는 총 점
problemcount = int(input())
for problemnum in range(problemcount):          #사용자가 입력한 문제들을 problem list에 넣는다
    problem[problemnum] = input()
while(correctnum!=problemcount):                #계산한 횟수가 입력한 문제의 개수와 동일해지면 점수 계산 프로그램은 종료된다.
    for correct in str(problem[correctnum]):    #사용자가 입력한 문제를 correct의 변수에 넣어 3가지 경우로 나눠 점수를 계산한다.
        if(correct=='O' and problemst==1):      # 1. 사용자가 연속해서 문제를 맞추고 있을 경우
            score+=plusscore                    #   총 점에 추가 점수를 더한다.
            plusscore+=1                        #   추가 점수는 계속 맞출 경우 1씩 증가한다.
            problemst=1                         #   사용자 상태는 1인 연속으로 맞추는 상태가 된다.
        elif(correct=='O' and problemst==0):    # 2. 사용자가 문제를 맞췄지만 이전에 틀렸거나 이번이 첫 문제인 경우
            score+=1                            # 기본 점수를 획득한다. 
            problemst=1                         # 이번에 문제를 맞췄기 때문에 사용자 상태는 이제 1이 된다.
        elif(correct=='X'):                     # 3. 사용자가 문제를 틀렸을 경우
            problemst=0                         # 사용자 상태는 0이 된다. 다음 문제시 추가 점수를 획득하지 못한다.
            plusscore=2                         # 추가 점수의 초기화
    print(score)        #총 점 출력
    score=0             #다음 problem list를 위한 총 점 초기화
    correctnum+=1       #다음 problem list를 계산하기 위해 증가