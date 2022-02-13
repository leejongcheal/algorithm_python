from typing import List
from collections import defaultdict
class Solution:
    def __init__(self):
        self.flag = 0
    def canFinish(self, numCourses: int,\
                  prer: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prer:
            graph[a].append(b)
        traced =set()
        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료후에 순환노드 삭제
            traced.remove(i)
            return 1
        for x in list(graph):
            # print(traced)
            # traced가 남아 있다면 전에 false가 떠서 remove를 제대로 못했다는 뜻
            # 그러나 역시 타임오버
            if not dfs(x) or traced:
                return False
        return True
# print(Solution().canFinish(5,[[1,4],[2,4],[3,1],[3,2]]))
print(Solution().canFinish(2,[[0,1]]))
