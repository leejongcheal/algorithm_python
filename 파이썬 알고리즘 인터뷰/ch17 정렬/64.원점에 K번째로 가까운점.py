from typing import List
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        temp = []
        for a, b in points:
            temp += [a**2 + b **2, a, b],
        temp.sort()
        result = []
        for i in range(k):
            dist, a, b = temp[i]
            result += [a, b],
        return result

k= 2
L =[[3,3],[5,-1],[-2,4]]
print(Solution().kClosest(L, k))

