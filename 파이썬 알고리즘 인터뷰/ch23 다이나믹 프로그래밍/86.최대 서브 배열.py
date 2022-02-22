from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        DP = [nums[0]]
        for i in range(1,len(nums)):
            DP.append(max(DP[-1]+ nums[i], nums[i]))
        return max(DP)


L = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(L))
