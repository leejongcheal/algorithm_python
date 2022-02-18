from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 피봇(제일 작은값 찾는 과정)
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] <= nums[right]:
                right = mid
        pivot = left
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_pivot = (mid + pivot) % len(nums)
            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        return -1




nums = [4,5,6,7,0,1,2]
target = 0


