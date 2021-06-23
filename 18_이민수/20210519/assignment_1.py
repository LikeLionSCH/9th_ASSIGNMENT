jpy = [500, 100, 50, 10, 5, 1]

pay = int(input())
change = 1000 - pay

count = 0
for i in jpy:
    count = count + change // i
    change = change % i

print(count)
