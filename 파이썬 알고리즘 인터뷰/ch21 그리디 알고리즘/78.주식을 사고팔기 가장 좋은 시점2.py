from collections import deque
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices) - 1))
        # res = 0
        # for i in range(len(prices) - 1):
        #     if prices[i+1] > prices[i]:
        #         res += prices[i+1] - prices[i]
        # return res

print(Solution().maxProfit([7,1,5,6,6,8]))