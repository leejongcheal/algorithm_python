from typing import List


class Solution:
    def findContentChildren(self, G: List[int], S: List[int]) -> int:
        G.sort(reverse=1)
        S.sort(reverse=1)
        res = 0
        while G and S:
            s = S.pop()
            if G[-1] <= s:
                G.pop()
                res += 1
        return res

g = [1,2]
s = [1,2,3]
print(Solution().findContentChildren(g, s))
