dic ={}

while True:
    print("===insert===")
    key = input("Key >> ")
    value = input("value >> ")
    dic[key]=value
    if(key=="cake"):
        break

print("===result===")
print(dic.values())