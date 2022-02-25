# (h*3600 + m*60 + s)*1000 + ms*1000
from collections import deque
import heapq

def solution(lines):
    # [start, end]값을 원소로
    L = []
    # start end 값 가져오기
    for line in lines:
        log = line.split()
        datetime = log[1]
        h = int(datetime[0:2])
        m = int(datetime[3:5])
        s = int(datetime[6:8])
        ms = int(datetime[9:12])
        processing_time = float(log[2][:-1])
        end = (h*3600 + m*60 + s)*1000 + ms
        start = end - (int(processing_time*1000) - 1)
        L.append([start, end])
    # if len(L) == 1:
    #     return 1
    L.sort()
    time_start = L[0][0]
    time_end = sorted(L, key=lambda x:-x[1])[0][1]
    time = time_start
    answer = 0
    now_request = 0
    q = []
    heapq.heappush(q,L[now_request][1])
    now_request = 0
    while time <= time_end:
        if not q:# and now_request + 1 < len(L):
            time = L[now_request + 1][0]
            heapq.heappush(q,(L[now_request+1][1]))
            now_request += 1
        elif q:
            while q and time > q[0]:
                heapq.heappop(q)
            while now_request + 1 < len(L) and time <= L[now_request + 1][0] < time + 1000:
                heapq.heappush(q,(L[now_request+1][1]))
                now_request += 1
            time += 1
        answer = max(answer, len(q))
    return answer


L = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
# L =  [
# "2016-09-15 01:00:04.002 2.0s"
# ]
print(solution(L))