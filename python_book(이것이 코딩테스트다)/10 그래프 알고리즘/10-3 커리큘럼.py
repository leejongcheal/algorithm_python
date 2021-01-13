from collections import deque
N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
cost = [0]*(N+1)
result = [0]*(N+1)
q = deque()
# (2) 10 1 -1 에서 1을 듣고 2를 들으라는 소리니 indegree 과정 거꾸로 하는 경우 조심
for i in range(1,N+1):
    L = list(map(int, input().split()))
    cost[i] = L[0]
    for j in range(1,len(L)):
        if L[j] != -1:
            graph[L[j]].append(i)
            indegree[i] += 1
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
        result[i] = cost[i]
while q:
    now = q.popleft()
    for des in graph[now]:
        if result[des] < result[now] + cost[des]:
            result[des] = result[now] + cost[des]
        indegree[des] -= 1
        if indegree[des] == 0:
            q.append(des)
for i in range(1, N+1):
    print(result[i])