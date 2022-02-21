from typing import List
import heapq
from collections import deque, Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_cnt = Counter(tasks)
        heap = []
        for key, cnt in tasks_cnt.items():
            heapq.heappush(heap,[-cnt, key])
        res = ""
        sub = 0
        while heap:
            temp = []
            sub = 0
            while heap and sub <= n:
                cnt, key = heapq.heappop(heap)
                if cnt + 1 != 0:
                    temp.append([cnt + 1, key])
                res += key
                sub += 1
            if temp:
                while sub <= n:
                    sub += 1
                    res += "0"
            for cnt, key in temp:
                heapq.heappush(heap,[cnt,key])
        # print(res)
        return len(res)




L =  ["A","A","A","B","B","B"]
print(Solution().leastInterval(L, 0))