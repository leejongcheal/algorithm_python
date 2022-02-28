from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        for price in prices:
            if price < min_price:
                min_price = price
            profit = max(profit, price - min_price)
        return profit


L = [7,1,5,3,6,4]
print(Solution().maxProfit(L))