from collections import deque

v, e = map(int ,input().split())
# 초기화
indegree = [0]*(v+1)
graph = [[] for _ in range(v+1)]
q = deque()
result = []
# 간선 입력 받으면서 진입차수 정리
for _ in range(e):
    a, b = map(int ,input().split())
    graph[a].append(b)
    indegree[b] += 1
# 위상 정렬
# 처음 진입차수 0인노드 큐에 삽입
for i in range(1,v+1):
    if indegree[i] == 0:
        q.append(i)
while q:
    now = q.popleft()
    result.append(now)
    # 연결된 간선 삭제 -> 연결된 정점의 진입차수 -1 if 0이면 큐에 삽입
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)
print(result)

