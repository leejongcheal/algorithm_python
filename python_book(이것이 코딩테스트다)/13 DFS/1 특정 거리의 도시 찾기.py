from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
res = []
visit = [0]*(N+1)
visit[X] = 1
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
q = deque()
q.append((X, 0))
visit[X] = 1
while q:
    now, dist = q.popleft()
    if dist == K:
        break
    for next in graph[now]:
        if visit[next] == 0:
            visit[next] = 1
            next_dist = dist + 1
            q.append((next, next_dist))
            if next_dist == K:
                res.append(next)
res.sort()
if res:
    for r in res:
        print(r)
else:
    print(-1)