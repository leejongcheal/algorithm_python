# (h*3600 + m*60 + s)*1000 + ms*1000
# https://programmers.co.kr/learn/courses/30/lessons/17676
import heapq
from collections import deque
def get_start_end(end_time, processing):
    h = int(end_time[:2])
    m = int(end_time[3:5])
    s = (float(end_time[6:]) * 1000)
    end = (h*3600 + m*60) * 1000 + s
    start = end + 1 - int(float(processing[:-1])*1000)
    return [start, end]
def solution(lines):
    L = []
    for line in lines:
        line = line.split()
        L.append(get_start_end(line[1], line[2]))
    L.sort()
    L = deque(L)
    res = 1
    end_list = []
    time = L[0][0]
    heapq.heappush(end_list, L[0][1])
    L.popleft()
    while L:
        while end_list and end_list[0] < time:
            heapq.heappop(end_list)
        while L and time + 999 >= L[0][0]:
            heapq.heappush(end_list, L.popleft()[1])
        res = max(res, len(end_list))
        time += 1
        # 다음 L값이 너무 먼 경우 ex 0시0분0초 시작 에서 23시59분59초 시작인경우 없으면 너무 많은 시간오버
        # 라서 추가함 -> 이런 생각은 무조건 했어야함 예시에서 걸려서 다행이지
        if not end_list:
            time = L[0][0]
            heapq.heappush(end_list, L.popleft()[1])

    return res





# L = [
# "2016-09-15 20:59:57.421 0.351s",
# "2016-09-15 20:59:58.233 1.181s",
# "2016-09-15 20:59:58.299 0.8s",
# "2016-09-15 20:59:58.688 1.041s",
# "2016-09-15 20:59:59.591 1.412s",
# "2016-09-15 21:00:00.464 1.466s",
# "2016-09-15 21:00:00.741 1.581s",
# "2016-09-15 21:00:00.748 2.31s",
# "2016-09-15 21:00:00.966 0.381s",
# "2016-09-15 21:00:02.066 2.62s"
# ]
# L = [
# "2016-09-15 00:00:01.000 0.9s",
# "2016-09-15 00:00:02.000 0.9s",
# "2016-09-15 00:00:03.000 0.9s",
# "2016-09-15 00:00:04.000 2.999s",
#     ]
L = ["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]
print(solution(L))