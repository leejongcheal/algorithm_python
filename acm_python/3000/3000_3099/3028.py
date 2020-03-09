a = 1
for c in input():
    if a == 1:
        if c == "A":
            a = 2
        if c == "C":
            a = 3
    elif a == 2:
        if c == "A":
            a = 1
        if c == "B":
            a = 3
    else:
        if c == "B":
            a = 2
        if c == "C":
            a = 1
print(a)