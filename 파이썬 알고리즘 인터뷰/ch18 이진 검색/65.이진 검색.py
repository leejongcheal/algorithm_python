from bisect import bisect_left, bisect_right

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if bisect_right(nums, target) - bisect_left(nums, target) > 0:
        #     return bisect_left(nums, target)
        # else:
        #     return -1
        index = bisect_left(nums, target)
        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1