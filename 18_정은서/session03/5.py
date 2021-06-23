x = int(input())
score = 0
count = 0

for i in range (x):
    case = list(input())
    for j in case:
        if j == 'O':
            count += 1
            score += count
        elif j == "X":
            count = 0
    print(score)
    score = 0
    count = 0
