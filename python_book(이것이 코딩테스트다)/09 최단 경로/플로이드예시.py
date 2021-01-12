INF = int(1e9)

# 노드의 개수 및 간선의 개수 입력받기
n, m = map(int, input().split())
# 2차원 리스트로 graph 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]
# 자기자신을 0 으로 초기화
for i in range(1,n+1):
    graph[i][i] = 0
# 원래 있는 값 입력 받아서 넣어주기
for i in range(m):
    print(i)
    a, b, c = map(int, input().split())
    graph[a][b] = c

for a in range(1,n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("X", end =" ")
        else:
            print(graph[a][b], end =" ")
    print()
# 점화식에 따른 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 출력
for a in range(1,n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("X", end =" ")
        else:
            print(graph[a][b], end =" ")
    print()
