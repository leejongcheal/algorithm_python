from collections import defaultdict
class Solution:
    def climbStairs(self, n: int) -> int:
        DP = defaultdict(int)
        DP[1] = 1
        DP[2] = 2
        for i in range(3,n+1):
            DP[i] = DP[i-1] + DP[i-2]
        return DP[n]

print(Solution().climbStairs(5))