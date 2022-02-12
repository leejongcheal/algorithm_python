from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # L = [i+1 for i in range(n)]
        # def comb(L, M):
        #     N = len(L)
        #     if N < M:
        #         return None
        #     ret = []
        #     if M == 1:
        #         for l in L:
        #             ret.append([l])
        #     else:
        #         for i in range(N - M + 1):
        #             for temp in comb(L[i+1:],M-1):
        #                 ret.append([L[i]]+temp)
        #     return ret
        # return comb(L,k)
        if n == 0 or n < k:
            return None
        res = []
        def dfs(index, now = []):
            if len(now) == k:
                res.append(now)
                return
            for i in range(index + 1, n + 1):
                dfs(i, now + [i])
        dfs(0)
        return res

print(Solution().combine(4, 2))
