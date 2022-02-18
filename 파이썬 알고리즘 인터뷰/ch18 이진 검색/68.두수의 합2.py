from typing import List
from bisect import bisect_left, bisect_right
# 답은 무조건 하나 + L은 정렬된 값이 들어옴
class Solution:
    def twoSum(self, L: List[int], target: int) -> List[int]:
        for start, val in enumerate(L):
            now_target = target - val
            index = bisect_left(L,now_target,start + 1)
            print(start, index)
            if index < len(L) and L[index] == now_target:
                return start + 1, index + 1
L = [0,0,1,2]
print(Solution().twoSum(L,0))