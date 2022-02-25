# https://programmers.co.kr/learn/courses/30/lessons/17680
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return 5*len(cities)
    q = deque(maxlen=cacheSize)
    for val in cities:
        val = val.lower()
        if val in q:
            answer += 1
            q.remove(val)
            q.append(val)
        else:
            answer += 5
            q.append(val)
    return answer

L = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(3, L))