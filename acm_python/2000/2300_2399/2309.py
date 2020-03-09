L = []
for i in range(9):
    L.append(int(input()))
L.sort()
s = sum(L[0:7])
M = 100 - s
if M != 0:
        for i in range(7, 9):  # 하나만 바꾸는 경우
            for m in range(0, 7):
                if L[i] - L[m] == M:
                    L[m] = L[i]
                    break
        if sum(L[:7]) != 100:
            for i in range(0, 6):
                if sum(L[:7]) == 100:
                    break
                for j in range(i+1, 7):
                    if L[8] - L[i] + L[7] - L[j] == M:
                        L[i] = L[8]
                        L[j] = L[7]
                        break

S = L[:7]
S.sort()
for i in S:
    print(i)
