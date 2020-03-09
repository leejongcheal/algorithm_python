N = int(input())
L = []
for i in range(N):
    L.append(str(input()))
length = len(L[0])
str = ""
for i in range(length):
    d = 0
    c = L[0][i]
    for j in range(1,N):
        if c != L[j][i]:
            d = 1
    if d == 0:
        str += c
    else:
        str += "?"
print(str)