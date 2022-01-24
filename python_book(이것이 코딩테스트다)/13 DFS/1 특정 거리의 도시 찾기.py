from collections import deque
N, M, K, start = map(int, input().split())
graph = [[]for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
q = deque()
q.append(start)
visit = [0]*(N+1)
visit[start] = 1
result = []
# BFS 시작
while q:
    now = q.popleft()
    if visit[now] == K + 1:
        result.append(now)
        continue
    for conneted_index in graph[now]:
        if visit[conneted_index] == 0:
            q.append(conneted_index)
            visit[conneted_index] = visit[now] + 1
    # 방문한적없는 경우에 q에 넣어주면 되겠네
result.sort()
if len(result) == 0:
    print(-1)
else:
    for i in result:
        print(i)