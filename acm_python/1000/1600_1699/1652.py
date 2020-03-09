N = int(input())
L = []
result_x = 0
result_y = 0
for i in range(N):
    L.append(input())
L1 = []
for i in range(N):
    s = ""
    for j in range(N):
        s += L[j][i]
    L1.append(s)
for i in range(N):
    X = L[i].split('X')
    Y = L1[i].split('X')
    for x in X:
        if len(x) >= 2:
            result_x += 1
    for y in Y:
        if len(y) >= 2:
            result_y += 1
print(result_x,result_y)
