# 이차원 리스트와 반복문

# 1. 이차원 리스트 만들기
example = []
num = 0

for i in range(5):
    k = []
    for j in range(5):
        k.append(j + num)
    num += 5
    example.append(k)

# 2. 원하는 부분만 출력
for i in example:
    print(i[1:4:2])