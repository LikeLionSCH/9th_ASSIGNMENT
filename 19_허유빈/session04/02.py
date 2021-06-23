list = []                    #빈 리스트 선언
num = 0                      #변수 선언

for i in range(5):           #5X5 이차원 리스트 생성
    e = []
    for j in range(5):
        e.append(num)        #num을 1씩 증가시켜 e에 추가
        num += 1             
    list.append(e)           #list에 e 추가
    i += 5                   #e리스트 입력마다 i 5씩 증가
# print(list)

for k in list:              #list만큼 반복
    print(k[1:4:2])         #1부터 3까지 2씩 증가하여 출력

# for k in range(5):
#     print(list[k][1:4:2])

# for k in range(5):
#     print(list[k][1], list[k][3])    #리스트 형식이 아닌 값만 출력