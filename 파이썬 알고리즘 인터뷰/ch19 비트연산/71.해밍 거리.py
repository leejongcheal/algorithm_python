from typing import List

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")

print(Solution().hammingDistance(2,4))