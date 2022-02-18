from typing import List

# 답은 무조건 하나 + L은 정렬된 값이 들어옴
class Solution:
    def twoSum(self, L: List[int], target: int) -> List[int]:
        left, right = 0, len(L) - 1
        while left < right:
            now_sum = L[left] + L[right]
            if now_sum > target:
                right -= 1
            elif now_sum < target:
                left += 1
            else:
                return (left + 1, right + 1)
L = [2,7,11,15]
print(Solution().twoSum(L,9))