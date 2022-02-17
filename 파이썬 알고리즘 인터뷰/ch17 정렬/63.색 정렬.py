from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> List:
        def quick_sort(L):
            if L == []:
                return []
            left = []
            right = []
            same = []
            mid = (0 + len(L) - 1) // 2
            pivot = L[mid]
            for l in L:
                if l < pivot:
                    left.append(l)
                elif l == pivot:
                    same.append(l)
                elif l > pivot:
                    right.append(l)
            return quick_sort(left) + same + quick_sort(right)
        return quick_sort(L)


L = [2,0,2,1,1,0]
print(Solution().sortColors(L))