n = int(input())  #테스트 횟수

for i in range(n):
    result = input()  # 퀴즈 결과
    result_list = list(result)  

    count = 0  # '0' 개수
    sum = 0  # 총합

    for i in result_list:
        if i == "x":
            count = 0
        else:
            count = count + 1
            sum = sum + count
        print(sum)