from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def findContentChildren(self, G: List[int], S: List[int]) -> int:
        G.sort()
        S.sort()
        res = 0
        for s in S:
            index = bisect_right(G,s)
            if index > res:
                res += 1
        return res


g = [1,2]
s = [1,2,3]
print(Solution().findContentChildren(g, s))
