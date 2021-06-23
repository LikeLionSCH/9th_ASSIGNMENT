problem = []
index = 0
R_index = 0
problem = input("O, X 문제를 입력하세요 >> ")

for i in problem:
    if (i == 'O'):
        index += 1
        R_index += index
    else:
        index = 0

print("최종 점수는", R_index, "입니다!")