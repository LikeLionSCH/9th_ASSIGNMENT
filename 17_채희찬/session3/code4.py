dictionary = {}
while True:
    print("===insert===")
    key = input("Key >> ")
    value = input("Value >> ")
    dictionary[key] = value
    if key=="cake":
        break

print("===result===")
for value in dictionary.values():
    print(value)