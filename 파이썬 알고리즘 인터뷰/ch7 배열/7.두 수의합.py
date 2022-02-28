from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i,val in enumerate(nums):
            dic[val] = i
        for i, num in enumerate(nums):
            complement = target - num
            ## [3,2,4] 6 인경우 3 3도 답일수 있으니 이에대한 예외처리 필요
            if complement in dic and i != dic[complement]:
                return [i, dic[complement]]
        # nums.sort()
        # start, end = 0, len(nums) - 1
        # while start < end:
        #     now = nums[start] + nums[end]
        #     if now == target:
        #         return [start, end]
        #     elif now < target:
        #         start += 1
        #     elif now > target:
        #         end -= 1

L = [3,2,4]
print(Solution().twoSum(L,6))