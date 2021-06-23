#1. 빈 딕셔너리를 생성
dic = {}
#2. 사용자로부터 key와 value를 입력받아 dictionary에 추가
while(True):
    print("===insert===")
    Key = str(input("Key >> "))
    value = str(input("value >> "))
    dic[Key] = value
    if (Key=="cake"):
        break
print("===result===")
#3. key값이 cake가 아니라면 2번으로 돌아감

#4. dictionary의 value값을 모두 출력
for i in dic.values():
    print(i)