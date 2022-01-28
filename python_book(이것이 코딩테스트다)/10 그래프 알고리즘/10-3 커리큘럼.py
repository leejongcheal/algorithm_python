from collections import deque
INF = int(1e10)
N = int(input())
indegree = [0]*N
# 해당 i -> j g[i] = j 꼴
graph = [[] for _ in range(N)]
# i -> j 일때 in_index[j] = i 꼴
in_index = [[] for _ in range(N)]
cost = [0]*N
# INF값으로 초기화했는데 그러면... max(res[now], cost + res[pre]) 처리를 못하자나..
res = [0]*N
result = 0
# 아무래도 문제가 있을수 있으니 스택대신 큐를 사용하는듯?
q = deque()
for i in range(N):
    L = list(map(int, input().split()))
    cost[i] = L[0]
    indegree[i] = len(L) - 2
    if indegree[i] == 0:
        q.append(i)
        res[i] = cost[i]
    for j in range(1, len(L)-1):
        in_index[i].append(L[j] - 1)
        graph[L[j] - 1].append(i)
while q:
    now = q.popleft()
    if len(in_index[now])!= 0:
        for in_ind in in_index[now]:
            res[now] = max(res[now], res[in_ind] + cost[now])
    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)
# 사실 grapp[now] 의 값이 없다는것은 끝점임으로 이점에 대해서만 max해서 구할려고함
# 그러나 어쩌피 제일 오래걸리는점이 끝점임은 자명함 따라서 max(res)로 바꿈
print(max(res))
