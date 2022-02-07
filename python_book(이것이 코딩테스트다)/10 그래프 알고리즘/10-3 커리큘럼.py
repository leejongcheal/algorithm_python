from collections import deque
N = int(input())
L = [[] for _ in range(N+1)]
time = [0]*(N+1)
indegree = [0]*(N+1)
q = deque()
result = []
for i in range(1, N + 1):
    l = list(map(int, input().split()))
    time[i] = l[0]
    indegree[i] = len(l) - 2
    if indegree[i] == 0:
        q.append(i)
    for j in range(1, len(l) - 1):
        pre = l[j]
        L[pre].append(i)
for i in range(N+1):
    result.append(time[i])
while q:
    now = q.popleft()
    for next in L[now]:
        indegree[next] -= 1
        result[next] = max(result[next], time[next] + result[now])
        if indegree[next] == 0:
            q.append(next)
for r in result[1:]:
    print(r)