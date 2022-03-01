from typing import List
from collections import defaultdict, Counter
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = defaultdict(list)
        N = len(tickets)
        # 그냥 map으로 쓰니깐 문제생기는데 list를 뺴먹었음
        tickets = list(map(tuple, tickets))
        visit_cnt = defaultdict(int)
        counter = Counter(tickets)
        for start, end in sorted(tickets):
            dic[start].append(end)

        def dfs(now, path=["JFK"]):
            if len(path) == N + 1:
                return path
            for next in dic[now]:
                if visit_cnt[(now, next)] < counter[(now, next)]:
                    visit_cnt[(now, next)] += 1
                    q = dfs(next, path + [next])
                    visit_cnt[(now, next)] -= 1
                    if q:
                        return q
            return None
        return dfs("JFK")


L = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],
 ["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
print(sorted(L))
print(Solution().findItinerary(L))