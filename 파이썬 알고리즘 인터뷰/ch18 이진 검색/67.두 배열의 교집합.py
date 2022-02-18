from typing import List
from bisect import bisect_left, bisect_right
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = j = 0
        res = set()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                res.add(nums1[i])
                i += 1
                j += 1
        return res

L1 = [4,9,5]
L2 = [9,4,9,8,4]
print(Solution().intersection(L1,L2))