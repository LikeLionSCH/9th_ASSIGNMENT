example = []
num = 0
for i in range(5):
    k = []
    for j in range(5):
        k.append(j+num)
    num += 5
    example.append(k)

#print(example)

for x in range(5):
    for y in range(5):
        if y % 2 != 0:
            print(example[x][y])