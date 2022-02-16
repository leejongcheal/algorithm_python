from typing import List
from collections import defaultdict, deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0]*n
        q = deque()
        cnt = n
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        for i in range(n):
            if indegree[i] == 1:
                q.append(i)
        while cnt > 2:
            cnt -= len(q)
            new_q = []
            for now in q:
                for next in graph[now]:
                    if indegree[next] > 0:
                        indegree[now] -= 1
                        indegree[next] -= 1
                        m = next
                        if indegree[next] == 1:
                            new_q.append(next)
            q = new_q
        if len(q) > 1:
            return q
        else:
            return [m]


n = 1
# edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# edges = [[1,0],[1,2],[1,3]]
edges = []
print(Solution().findMinHeightTrees(n, edges))