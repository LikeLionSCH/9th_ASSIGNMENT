# 사용자가 key 값으로 cake를 입력할 때까지 key와 value를 계속 입력받아 dictionary에 추가하고, dictionary의 전체 value 값을 출력하는 코드를 작성하세요.
# 1. 빈 dictionary를 만든다.
# 2. 사용자로부터 key와 value를 입력받아 dictionary에 추가한다.
# 3. key 값이 cake가 아니라면 2번으로 돌아간다.
# 4. dictionary의 value 값을 모두 출력한다.
food = {}

while True:
    print("===insert===")
    input1 = input('Key >> ')
    input2 = input('value >> ')
    food[input1] = input2
    if input1 == 'cake':
        break


print("===result===")
for i in food.values():
    print(i)