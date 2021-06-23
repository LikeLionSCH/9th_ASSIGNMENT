dictionary = {}

while(True):
    print("===insert===")
    print("Key >> ",end="")
    key = input()
    print("value >> ",end="")
    value = input()    
    dictionary[key] = value
    if(key == 'cake'):
        break
        
print("===result===")
for value in dictionary.values():
    print(value)