import heapq
N = int(input())
L = []
for _ in range(N):
    heapq.heappush(L,int(input()))
res = 0
while len(L) >= 2:
    a = heapq.heappop(L)
    b = heapq.heappop(L)
    res += a + b
    heapq.heappush(L,a+b)
print(res)