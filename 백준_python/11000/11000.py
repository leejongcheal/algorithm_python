import sys,heapq
n = int(input())
h = []
for i in sys.stdin.read().splitlines():
    heapq.heappush(h,list(map(int,i.split())))
res = [0]
for i in range(n):
    c = 0
    L = heapq.heappop(h)
    if res[0] <= L[0]:
        heapq.heapreplace(res, L[1])
    elif res[0] > L[0]:
        heapq.heappush(res, L[1])
print(len(res))
