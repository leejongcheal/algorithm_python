from typing import List
import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        INF = int(1e10)
        graph = defaultdict(list)
        for a,b,w in flights:
            graph[a].append((b,w))
        res = [INF]*(n)
        res[src] = 0
        q = [(0, src, 0)]
        while q:
            now_dist, now, k = heapq.heappop(q)
            if k > K:  # res[now] < now_dist일 경우도 돌아야함 k 기준으로 탐색해야하니
                continue
            for next, dist in graph[now]:
                next_dist = dist + now_dist
                if res[next] > next_dist:
                    res[next] = next_dist
                # 안쪽일 경우에만 값이 제일 작고 k내일때 res 수정
                # 검사는 k의 기준에 따라서 작은값을 넣어주는식으로 탐색
                heapq.heappush(q,(next_dist, next, k + 1))
        if res[dst] >= INF:
            return -1
        else:
            return res[dst]
print(Solution().findCheapestPrice(5, [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],0,2,2))