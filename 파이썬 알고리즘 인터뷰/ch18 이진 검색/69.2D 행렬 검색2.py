from typing import List
from bisect import bisect_left
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        temp = []
        for row in matrix:
            index = bisect_left(row,target)
            if index < len(row) and row[index] == target:
                return True
        return False

L  = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print(Solution().searchMatrix(L,0))
