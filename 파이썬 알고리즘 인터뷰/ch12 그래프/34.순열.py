from typing import List
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(list,permutations(nums, len(nums))))


print(Solution().permute([1,2,3]))