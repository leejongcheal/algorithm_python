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
        visit = set()
        while q:
            now_dist, now, k = heapq.heappop(q)
            if (now, k) in visit:
                continue
            visit.add((now, k))
            # 결국엔 dst를 제일 먼저 오는것은 k내의 제일 작은 dist를 가진값이므로 이런식으로 리턴 해도 정답임
            if now == dst:
                return now_dist
            # 현재 k는 다음에 방문할 노드의 현재 경유지 갯수를 뜻함 -> 따라서 조건문 전에 dst이면 상관없음
            if k > K:  # res[now] < now_dist일 경우도 돌아야함 k 기준으로 탐색해야하니
                continue
            for next, dist in graph[now]:
                next_dist = dist + now_dist
                if res[next] > next_dist:
                    res[next] = next_dist
                # 안쪽일 경우에만 값이 제일 작고 k내일때 res 수정
                # 검사는 k의 기준에 따라서 작은값을 넣어주는식으로 탐색
                heapq.heappush(q,(next_dist, next, k + 1))
        return -1
print(Solution().findCheapestPrice(5, [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],0,2,2))