numList = [
    [0,1,2,3,4],
    [5,6,7,8,9],
    [10,11,12,13,14],
    [15,16,17,18,19],
    [20,21,22,23,24]
]

for i in range(len(numList)) :
    for j in range(len(numList[i])) :
        if j%2 == 1 :
            print(numList[i][j], end=' ')