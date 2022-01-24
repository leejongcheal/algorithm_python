import heapq

INF = int(1e9)
N, M = map(int, input().split())
Map = []
res = [[INF] * M for _ in range(N)]
for _ in range(N):
    Map.append(list(map(int, input().split())))
steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
q = []
heapq.heappush(q, (1, 0, 0))
while q:
    dist, x, y = heapq.heappop(q)
    if res[x][y] < dist:
        continue
    for i in range(4):
        nx, ny = x + steps[i][0], y + steps[i][1]
        if 0 <= nx < N and 0 <= ny < M:
            if Map[nx][ny] == 1:
                target_dist = res[x][y] + 1
                if target_dist < [nx][ny]:
                    res[nx][ny] = target_dist
                    heapq.heappush(q, (res[nx][ny], nx, ny))
print(res[N - 1][M - 1])
