from typing import List
from collections import defaultdict
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        DP = defaultdict(int)
        DP[1] = nums[0]
        for i in range(1,len(nums)):
            DP[i+1] = max(DP[i],DP[i-1] + nums[i])
        return DP[len(nums)]

L = [2,7,9,3,1]
print(Solution().rob(L))