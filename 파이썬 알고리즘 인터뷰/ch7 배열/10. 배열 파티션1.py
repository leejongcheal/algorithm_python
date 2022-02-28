from typing import List



class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # nums.sort()
        # res = 0
        # for i in range(len(nums) //2 ):
        #     res += nums[2*i]
        # return res
        return sum(sorted(nums)[::2])
        # 나의 한계
        # return sum([val for i, val in enumerate(sorted(nums)) if i % 2 == 0])

print(Solution().arrayPairSum([6,2,6,5,1,2]))