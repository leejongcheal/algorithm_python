from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(csum, index, path):
            if csum == 0:
                res.append(path)
                return
            elif csum < 0:
                return
            else:
                for i in range(index,len(candidates)):
                    dfs(csum - candidates[i],i,path + [candidates[i]])
        res = []
        dfs(target, 0, [])
        return res

print(Solution().combinationSum([2,7,6,3,5,1], 9))