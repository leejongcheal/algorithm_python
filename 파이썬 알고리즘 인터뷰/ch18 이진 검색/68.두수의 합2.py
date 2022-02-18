from typing import List
from bisect import bisect_left, bisect_right
# 답은 무조건 하나 + L은 정렬된 값이 들어옴
class Solution:
    def twoSum(self, L: List[int], target: int) -> List[int]:
        for start, val in enumerate(L):
            now_target = target - val
            temp = L[start+1:]
            index = bisect_left(temp, now_target)
            if index < len(temp) and L[index + start + 1] == now_target:
                return start + 1, start + index + 2
L = [5, 25, 75]
print(Solution().twoSum(L,100))