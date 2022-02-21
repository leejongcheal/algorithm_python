from collections import deque
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        res = 0
        q = deque([])
        for p in prices:
            if not q:
                q.append(p)
            elif q and q[-1] > p:
                res += q[-1] - q[0]
                q = []
                q.append(p)
            elif q and q[-1] < p:
                q.append(p)
        if q:
            res += q[-1] - q[0]
        return res

print(Solution().maxProfit([7,1,5,3,6,4]))