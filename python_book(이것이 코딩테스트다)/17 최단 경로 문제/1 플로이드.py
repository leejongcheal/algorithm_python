INF = int(1e9)
N = int(input())
M = int(input())
Map = [[INF]*(N+1) for _ in range(N+1)]
for i in range(N+1):
    Map[i][i] = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    Map[a][b] = min(c, Map[a][b])
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            Map[i][j] = min(Map[i][k] + Map[k][j], Map[i][j])
for i in range(1, N+1):
    for j in range(1, N+1):
        if Map[i][j] >= INF:
            Map[i][j] = 0
        print(Map[i][j], end=' ')
    print()

