from collections import Counter
from typing import List
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return list(zip(*Counter(nums).most_common(k)))[0]
        return list(zip(*Counter(nums).most_common(k)))[0]


print(Solution().topKFrequent([1,1,1,2,2,2,2,3],2))