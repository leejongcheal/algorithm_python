from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        result = []
        for start, last in sorted(intervals):
            if result and start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], last)
            else:
                result += [start,last],
                # result += [[start, last]]
                # result.append([start, last])
        return result

intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,3]]
print(Solution().merge(intervals))