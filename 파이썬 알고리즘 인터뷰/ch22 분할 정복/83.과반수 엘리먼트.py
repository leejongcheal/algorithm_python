from typing import List
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]

L = [3,2,3,2,3]
print(Solution().majorityElement(L))