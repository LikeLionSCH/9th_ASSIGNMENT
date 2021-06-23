dic = {}
value_list = []

while True : 
    print("===insert===")
    key = input("Key >> ")
    value = input("value >> ")
    dic[key] = value
    value_list.append(value)
    
    if 'cake' in dic.keys():
        break

print("===result===")
print(value_list)