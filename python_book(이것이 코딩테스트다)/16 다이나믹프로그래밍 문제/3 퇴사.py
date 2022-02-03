N = int(input())
L = []
for _ in range(N):
    L.append(list(map(int ,input().split())))
D = [0]*(N + 1)
for i in range(1, N+1):
    D[i] = D[i - 1]
    for j in range(0, i):
        if i >= j + L[j][0]:
            D[i] = max(D[j] + L[j][1], D[i])
print(D[N])