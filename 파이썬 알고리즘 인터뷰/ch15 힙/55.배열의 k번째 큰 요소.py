from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap,-n)
        for i in range(k):
            res = heapq.heappop(heap)
        return -res


print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))