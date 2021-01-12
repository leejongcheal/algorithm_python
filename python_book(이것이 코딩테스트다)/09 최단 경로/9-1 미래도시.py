INF = int(1e9)
N, M = map(int, input().split())
graph = [[INF]*(N+1) for _ in range(N+1)]
# 입력 받기 + 양방향
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
X, K = map(int, input().split())
# 자기 자신 0으로 넣기
for i in range(1,N+1):
    graph[i][i] = 0
# 플로이드 워셜
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
# 못가는 경우 예외처리 -1출력
result_distance = graph[1][K] + graph[K][X]
if result_distance >= INF:
    print(-1)
else:
    print(result_distance)