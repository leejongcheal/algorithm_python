from typing import List
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(path):
            now = path[-1]
            if len(path) == N:
                return path[:]
            temp = graph[now][:]
            for next in temp:
                graph[now].remove(next)
                a = dfs(path + [next])
                if a is not None:
                    return a
                graph[now].append(next)
                graph[now].sort()
            return None
        tickets.sort()
        graph = defaultdict(list)
        N = len(tickets) + 1
        for a, b in tickets:
            graph[a].append(b)
        return dfs(["JFK"])



print(Solution().findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))