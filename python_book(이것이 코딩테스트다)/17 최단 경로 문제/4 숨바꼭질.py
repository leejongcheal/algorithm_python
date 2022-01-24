import heapq

INF = int(1e9)
N, M = map(int, input().split())
L = [[] for _ in range(N + 1)]
res = [INF] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    L[a].append(b)
    L[b].append(a)
q = []
heapq.heappush(q, (0, 1))
res[1] = 0
while q:
    value, k = heapq.heappop(q)
    if res[k] < value:
        continue
    for t in L[k]:
        dist = value + 1
        if res[t] > dist:
            res[t] = dist
            heapq.heappush(q, (res[t], t))
max_value = max(res[2:])
max_cnt = 0
max_index = INF
for i in range(1,N+1):
    if res[i] == max_value:
        max_index = min(max_index, i)
        max_cnt += 1
print(max_index, max_value, max_cnt)
print(res)