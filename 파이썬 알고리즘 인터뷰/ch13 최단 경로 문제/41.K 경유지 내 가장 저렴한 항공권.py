from typing import List
import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        INF = int(1e10)
        dist_list = defaultdict(int)
        graph = defaultdict(list)
        res = [] # k개 이내에 dist에 도착한 경우에 추가
        q = [(0, src, -1)]
        for a,b,c in flights:
            graph[a].append((b, c))
        while q:
            dist, now, k = heapq.heappop(q)
            if k > K or (dist_list[(now, k)] != 0 and dist_list[(now, k)] < dist):
                continue
            # k는 위에서 걸리는 조사할 필요없고, 한번이라도 나오는경우가 제일 작은값이니 바로 return해준다.
            if now == dst:
                res.append(dist)
                continue
            # 이렇게 생략할려고 했는데 복잡해지는경우 답이 아닐수도 있음
            # if now == dst:
            #     return dist
            if dist < dist_list[(now, k)]:
                continue
            for next, val in graph[now]:
                if dist_list[(next, k+1)] == 0 or dist + val < dist_list[(next, k+1)]:
                    dist_list[(next, k+1)] = dist + val
                    heapq.heappush(q, (dist_list[(next, k+1)], next, k + 1))
        if res:
            return min(res)
        else:
            return -1
# 5, [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],0,2,2 // 7
# 5,[[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]],0,4,1 //  5
print(Solution().findCheapestPrice(5,[[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]],0,4,1))
