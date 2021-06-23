# 5x5(0~24)의 1,3번째 column 요소만 출력

# 5x5 행렬 리스트 생성
list=[]
num=0

for r in range(5):
    k=[]
    for c in range(5):
        k.append(num)
        num+=1
    list.append(k)
    # print(k) # 각 열의 5개 요소를 출력

for r in range(5):
    for c in range(5):
        if c==1 or c==3: # 열의 인덱스가 1 또는 3인 경우
            n=c # 해당하는 1 또는 3의 숫자를 n에 대입
            print(list[r][n]) # 해당 row의 n번째 col 요소를 출력