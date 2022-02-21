from typing import List
import heapq
from collections import deque, Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        result = 0
        while True:
            sub = 0
            for task, _ in counter.most_common(n+1):
                sub += 1
                result += 1
                counter[task] -= 1
                counter += Counter()
            if not counter:
                break
            result += (n + 1 - sub)

        return result



L =  ["A","A","A","B","B","B","B","B"]
print(Solution().leastInterval(L, 1))