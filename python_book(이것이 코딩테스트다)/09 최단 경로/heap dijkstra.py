import heapq
INF = int(1e9)
n, m = map(int, input().split())
start = int(input())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))

q = []
res = [INF]*(n+1)
heapq.heappush(q,(0,start))
res[start] = 0
while q:
    print(q)
    dist, index = heapq.heappop(q)
    if res[index] < dist:
        continue
    for i in g[index]:
        if res[i[0]]> dist + i[1]:
            res[i[0]] = dist + i[1]
            heapq.heappush(q,(res[i[0]],i[0]))
for i in res:
    print(i)