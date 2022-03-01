from typing import List
import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = int(1e10)
        graph = defaultdict(list)
        for a,b,c in times:
            graph[a].append((c, b))
        res = [INF]*(n+1)
        res[0], res[k] = 0, 0
        q = [(0, k)]
        while q:
            dist, now = heapq.heappop(q)
            # 다익스트라 다중방문 제거
            if dist > res[now]:
                continue
            for val, next in graph[now]:
                if dist + val < res[next]:
                    res[next] = dist + val
                    heapq.heappush(q,(res[next], next))
        if INF in res:
            return -1
        return max(res)
print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))
print(Solution().networkDelayTime([[1,2,1]],2,2))
