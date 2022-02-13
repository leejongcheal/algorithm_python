from typing import List
import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for a, b, c in times:
            graph[a].append((b,c))
        res = [-1]*(n+1)
        res[k] = 0
        q = []
        heapq.heappush(q,(res[k],k))
        while q:
            now_dist, now = heapq.heappop(q)
            if now_dist < res[now]:
                continue
            for next, dist in graph[now]:
                next_dist = dist + now_dist
                if res[next] == -1 or next_dist< res[next]:
                    res[next] = next_dist
                    heapq.heappush(q,(next_dist, next))
        if -1 in res[1:n+1]:
            return -1
        return max(res[1:n+1])

print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))
print(Solution().networkDelayTime([[1,2,1]],2,2))


