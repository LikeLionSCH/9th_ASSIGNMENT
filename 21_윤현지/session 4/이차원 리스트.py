list = [[0]*5 for _ in range(5)]
num=0

for i in range(5):
    for j in range(5):
        list[i][j]=j+num

    num +=5

result1=[]
result2=[]

for l in list[0:]:
    result1.append(l[1])
for e in list[0:]:
    result2.append(e[3])

print(result1)
print(result2)