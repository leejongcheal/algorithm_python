from typing import List
from bisect import bisect_left, bisect_right
# 답은 무조건 하나 + L은 정렬된 값이 들어옴
class Solution:
    def twoSum(self, L: List[int], target: int) -> List[int]:
        for start in range(len(L) - 1):
            now_target = target - L[start]
            index = bisect_left(L[start+1:],now_target)
            if index + start + 1< len(L) and L[index + start + 1] == now_target:
                return (start + 1, index + start + 2)
L = [2,7,11,15]
print(Solution().twoSum(L,9))