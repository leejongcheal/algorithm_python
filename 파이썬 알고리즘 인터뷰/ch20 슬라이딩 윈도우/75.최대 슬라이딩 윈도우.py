from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        INF = int(1e10)
        now_max = -INF
        window = deque()
        res = []
        for index, val in enumerate(nums):
            window.append(val)
            if index < k - 1:
                continue
            if now_max == -INF:
                now_max = max(window)
            else:
                now_max = max(now_max, val)
            res.append(now_max)
            if now_max == window.popleft():
                now_max = -INF
        return res

L = [1,3,-1,-3,5,3,6,7]
print(Solution().maxSlidingWindow([1,2],1))