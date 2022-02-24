# https://programmers.co.kr/learn/courses/30/lessons/17680
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return 5*len(cities)
    q = deque([])
    for index, val in enumerate(cities):
        val = val.lower()
        if val in q:
            q.remove(val)
            q.append(val)
            answer += 1
        else:
            if q and len(q) >= cacheSize:
                q.popleft()
            q.append(val)
            answer += 5
    return answer