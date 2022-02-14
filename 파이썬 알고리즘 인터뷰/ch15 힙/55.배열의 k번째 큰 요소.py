from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(len(nums) - k):
            heapq.heappop(nums)
        return heapq.heappop(nums)



print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))