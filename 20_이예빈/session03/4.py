fruit={}    # "fruit" 이름의 빈 딕셔너리 생성

while(1):
    print("===insert===")   # key, value 값 입력 받음
    key=input("Key >> ")
    value=input("Value >> ")
    if(key=="cake"):    # key값이 "cake"과 같다면 반복문을 빠져나옴
        break
    fruit[key]=value    # insert

print(fruit)    # fruit 딕셔너리 출력