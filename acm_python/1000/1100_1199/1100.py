r = 0
for i in range(8):
    c = input()
    for j in range(8):
        if (i+j) % 2 == 0 and c[j] == "F":
            r += 1
print(r)
