from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        L = [gas[i]-cost[i] for i in range(len(gas))]
        if sum(L) < 0:
            return -1
        L = L*2
        head, tail = 0, 0
        fuel = L[0]
        while head < len(gas) and tail < len(L):
            if tail - head == len(gas) - 1:
                return head
            if head > tail:
                tail = head
                fuel = L[head]
            if fuel >= 0:
                tail += 1
                fuel += L[tail]
            elif fuel < 0:
                fuel -= L[head]
                head += 1
        return -1
# 결국엔 틀린 풀이인데 위랑 차이점 잘 눈여겨보기
# tail += 1 하고 fuel + L[tail]로 조건문 따졌는데 이부분에서 조금 잘못됨
#  head, tail = 0, -1
#         fuel = 0
#         while head < len(gas) and tail < 2*len(gas):
#             if tail - head == len(gas) - 1:
#                 return head
#             tail += 1
#             if fuel + L[tail] > 0:
#                 fuel += L[tail]
#             else:
#                 # 최소한 head == tail이면 0의값을 가짐
#                 while fuel < 0: #and head < tail:
#                     fuel -= L[head]
#                     head += 1
#                 if head == tail:
#                     head += 1
#                     fuel = 0



gas =  [1,2,3,4,5]
cost = [3,4,5,1,2]
print(Solution().canCompleteCircuit(gas, cost))

