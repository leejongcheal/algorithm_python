from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []
        res = []
        def dfs(start, now = []):
            res.append(now)
            for i in range(start,len(nums)):
                dfs(i + 1, now + [nums[i]])
        dfs(0)
        return res

print(Solution().subsets([1,2,3]))