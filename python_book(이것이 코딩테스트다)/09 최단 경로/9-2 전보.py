import heapq
INF = int(1e9)
N, M, start = map(int, input().split())
result = [INF]*(N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
q = []
heapq.heappush(q, (0, start))
result[start] = 0
while q:
    now_dist, now = heapq.heappop(q)
    if now_dist > result[now]:
        continue
    for destination, now_des_dist in graph[now]:
        cost = now_dist + now_des_dist
        if cost < result[destination]:
            result[destination] = cost
            heapq.heappush(q, (cost, destination))
count = -1
cost = []
for i in range(1,N+1):
    if result[i] != INF:
        count += 1
        cost.append(result[i])
print(count, max(cost))

