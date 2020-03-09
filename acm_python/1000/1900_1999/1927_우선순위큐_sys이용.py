import heapq
import sys
N = int(input())
q = []
a = list(map(int,sys.stdin.read().splitlines()))
ans = ""
for i in range(N):
    if a[i] == 0:
        if len(q) == 0:
            ans += "0\n"
        else:
            ans += str(heapq.heappop(q))+"\n"
    else:
        heapq.heappush(q,a[i])
print(ans)
