my_list = []
n = 0

for i in range(5):
    temp = []
    for j in range(5):
        temp.append(j + n)
    n += 5
    my_list.append(temp)

for i in range(len(my_list[0:])):
    for j in range(len(my_list[0:])):
        if j % 2 != 0:
            print(my_list[i][j])


