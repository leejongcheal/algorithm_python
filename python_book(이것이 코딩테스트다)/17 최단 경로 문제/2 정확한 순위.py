INF = int(1e9)
N, M = map(int, input().split())
L = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    L[a][b] = 1
for i in range(1, N+1):
    L[i][i] = 0
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            L[i][j] = min(L[i][j], L[i][k] + L[k][j])
# 갯수 세기
result = 0
for i in L:
    print(i)
for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if L[i][j] < INF or L[j][i] < INF:
            cnt += 1
    if cnt == N:
        result += 1
print(result)