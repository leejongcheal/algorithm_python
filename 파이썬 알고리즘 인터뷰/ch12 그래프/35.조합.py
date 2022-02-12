from typing import List

from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        L = [i+1 for i in range(n)]
        return list(combinations(L,k))

print(Solution().combine(4, 2))
