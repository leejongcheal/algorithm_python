from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start, fuel = 0 , 0
        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                start, fuel = i+1, 0
            else:
                fuel += gas[i] - cost[i]
        return start

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(Solution().canCompleteCircuit(gas, cost))

