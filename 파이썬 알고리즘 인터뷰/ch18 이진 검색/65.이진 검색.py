from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(start, end):
            if start > end:
                return -1
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_search(start, mid - 1)
            else:
                return binary_search(mid + 1, end)

        return binary_search(0,len(nums) - 1)

L =  [-1,0,3,3,5,9,12]
# intervals = [[1,3]]
print(Solution().search(L,1))