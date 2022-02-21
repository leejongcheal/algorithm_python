from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        for start in range(len(gas)):
            fuel = 0
            for i in range(start, len(gas) + start):
                index = i % len(gas)
                flag = 1
                if gas[index] + fuel < cost[index]:
                    flag = 0
                    break
                else:
                    fuel += gas[index] - cost[index]
            if flag:
                return start
        return -1

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(Solution().canCompleteCircuit(gas, cost))

