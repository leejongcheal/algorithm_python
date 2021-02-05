INF = int(1e9)
N, M = map(int, input().split())
Map = [[INF]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    L = list(map(int, input().split()))
    for j in range(N):
        if L[j] == 1:
            Map[i][j+1] = 1
move = list(map(int, input().split()))
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            Map[i][j] = min(Map[i][j], Map[i][k] + Map[k][j])
flag = 0
for i in range(len(move) - 1):
    if Map[move[i]][move[i+1]] >= INF:
        flag = 1
if flag == 1:
    print("NO")
else:
    print('YES')

