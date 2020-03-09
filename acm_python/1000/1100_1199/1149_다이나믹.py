n = int(input())
L = []
for i in range(n):
    L.append(list(map(int, input().split())))
R = []
for i in range(n):
    if i == 0:
        R.append(L[i])
    else:
        C = []
        # 지금 r선택하는경우
        if R[i - 1][1] + L[i][0] > R[i - 1][2] + L[i][0]:
            C.append(R[i - 1][2] + L[i][0])
        else:
            C.append(R[i - 1][1] + L[i][0])
        # G
        if R[i - 1][0] + L[i][1] > R[i - 1][2] + L[i][1]:
            C.append(R[i - 1][2] + L[i][1])
        else:
            C.append(R[i - 1][0] + L[i][1])
        # B
        if R[i - 1][1] + L[i][2] > R[i - 1][0] + L[i][2]:
            C.append(R[i - 1][0] + L[i][2])
        else:
            C.append(R[i - 1][1] + L[i][2])
        R.append(C)
print(min(R[i]))