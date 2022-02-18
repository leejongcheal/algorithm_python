from typing import List
from bisect import bisect_left, bisect_right
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        res = set()
        for data in set(nums2):
            if bisect_right(nums1, data) - bisect_left(nums1,data) > 0:
                res.add(data)
        return res

L1 = [4,9,5]
L2 = [9,4,9,8,4]
print(Solution().intersection(L1,L2))