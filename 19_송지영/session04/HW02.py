a = []
r = 0

for i in range(5):
    b = []
    for j in range(5):
        b.append(r)
        r += 1
    i += 5

    a.append(b)

for c in range(5):
    print(a[c][1],a[c][3])