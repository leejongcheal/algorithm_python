N = int(input())
L = []
for _ in range(N):
    L.append(list(map(int, input().split())))
for i in range(1,N):
    for j in range(0, i + 1):
        if j == 0:
            L[i][j] = L[i-1][j]+ L[i][j]
        elif j == i:
            L[i][j] = L[i-1][j-1]+ L[i][j]
        else:
            L[i][j] = max(L[i-1][j], L[i-1][j-1]) + L[i][j]
print(max(L[N-1]))