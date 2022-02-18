from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, ans = deque(), []
        for index, val in enumerate(nums):
            if q and index - q[0][0] == k:
                q.popleft()
            while q and q[-1][1] < val:
                q.pop()
            q.append((index, val))
            if index >= k - 1:
                ans.append(q[0][1])
        return ans

sol = Solution()
print(sol.maxSlidingWindow(nums=[1,-1], k=1))