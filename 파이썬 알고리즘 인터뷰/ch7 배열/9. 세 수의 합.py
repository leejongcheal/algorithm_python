from typing import List
from itertools import combinations


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        # print(nums)
        nums.sort()
        res = []
        # print(nums)
        for k in range(len(nums) - 2):
            # print(k)
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            left = k + 1
            right = len(nums) - 1
            # print(right)
            while left < right:
                print(left, right)
                sum = nums[k] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    res.append([nums[k], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]), "CC")
