from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(now):
            if len(now) == len(nums):
                res.append(now)
                return
            for index, n in enumerate(nums):
                if visit[index]:
                    visit[index] -= 1
                    dfs(now+[n])
                    visit[index] += 1
        res = []
        visit = [1]*len(nums)
        dfs([])
        return res
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     def perm(L, M):
    #         N = len(L)
    #         if N < M:
    #             return None
    #         ret = []
    #         if M == 1:
    #             for l in L:
    #                 ret.append([l])
    #         else:
    #             for i in range(N):
    #                 for temp in perm(L[:i]+L[i+1:],M-1):
    #                     ret.append(temp + [L[i]])
    #         return ret
    #     return perm(nums, len(nums))


print(Solution().permute([1,2,3]))