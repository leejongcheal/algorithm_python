from typing import List
from itertools import combinations


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        prev = -(1e10)
        for i in range(len(nums)-2):
            # 중복 제거위함
            if prev == nums[i]:
                continue
            prev = nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                now = nums[i] + nums[left] + nums[right]
                if now == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # 요기를 잘못생각함
                    left += 1
                    right -= 1
                elif now < 0:
                    left += 1
                elif now > 0:
                    right -= 1
        return res






print(Solution().threeSum([-2,0,0,2,2]), "CC")
# print(Solution().threeSum([-1, 0, 1, 2, -1, -4, -1]), "CC")