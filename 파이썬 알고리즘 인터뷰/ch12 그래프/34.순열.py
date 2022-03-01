from typing import List
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
                return
            for n in nums:
                # 이부분을 visit 으로 처리하면 2배 빨라짐 -> 이거를 상기**
                if n not in path:
                    dfs(path + [n])
        dfs([])
        return res


print(Solution().permute([1,2,3]))