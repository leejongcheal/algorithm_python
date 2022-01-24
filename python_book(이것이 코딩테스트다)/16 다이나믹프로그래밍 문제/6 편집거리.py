N = input()
M = input()
n = len(N)
m = len(M)
L = [[0]*(m+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(m+1):
        if i == 0 or j == 0:
            L[i][j] = i+j
            continue
        if N[i-1] == M[j-1]:
            L[i][j] = L[i-1][j-1]
        else:
            L[i][j] = min(L[i-1][j-1], L[i][j-1], L[i-1][j]) + 1
print(L[n][m])