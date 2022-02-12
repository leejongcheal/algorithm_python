from typing import List
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)

        route = []
        def dfs(a):
            # 첫 번째 값을 읽어 어휘순 방문
            while graph[a]:
                # pop 연산을 통해서 재방문하는 경우도 제한함
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')
        # 다시 뒤집어 어휘순 결과로
        return route[::-1]


print(Solution().findItinerary([["JFK","KUL"],["JFK","NRT"],["KUL","JFK"]]))
