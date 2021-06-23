dic = {}

while(True):
    print("===insert===")
    key = input("Key >> ")
    value = input("value >> ")

    dic[key] = value
    
    if(key == "cake"):
        break

print("===result===")
for value in dic.values():
    print(value)