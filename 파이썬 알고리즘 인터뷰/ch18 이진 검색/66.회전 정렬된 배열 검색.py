from typing import List
from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 피봇(제일 작은값 찾는 과정)
        pivot_value = min(nums)
        pivot = nums.index(pivot_value)
        L = nums[pivot:] + nums[:pivot]
        index = bisect_left(L, target)
        if index < len(nums) and L[index] == target:
            return (pivot + index) % len(nums)
        else:
            return -1

nums = [4,5,6,7,0,1,2]
# nums = [1]
target = 0
print(Solution().search([3,1], 3))