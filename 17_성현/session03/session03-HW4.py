dic = {}
print('===insert===')
num =0
while(True):
    print('key >> ',end='')
    key = input()
    print('value >> ',end='')
    value = input()
    dic[str(key)] = value
    print(dic.items())
    num+=1
    if key=='cake':
        break
print('===result===')
for count in range(num) :
    print(format(list(dic.values())[count]))