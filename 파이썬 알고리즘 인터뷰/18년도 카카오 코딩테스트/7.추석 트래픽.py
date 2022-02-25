# (h*3600 + m*60 + s)*1000 + ms*1000
from collections import deque
import heapq
def get_times(datetime, prosessing_log):
    h = int(datetime[0:2])
    m = int(datetime[3:5])
    s = int(datetime[6:8])
    ms = int(datetime[9:12])
    processing_time = float(prosessing_log[:-1])
    end = (h * 3600 + m * 60 + s) * 1000 + ms
    start = end - (int(processing_time * 1000) - 1)
    return [start, end]

def solution(lines):
    # [start, end]값을 원소로
    L = []
    # start end 값 가져오기
    for line in lines:
        log = line.split()
        L.append(get_times(log[1], log[2]))
    # 완료시간순으로 인풋값이 들어오니
    time_end = L[-1][1]
    # time_end = sorted(L, key=lambda x: -x[1])[0][1]
    L.sort()
    time = L[0][0]
    answer = 0
    now_request = 0
    q = []
    heapq.heappush(q,L[now_request][1])
    now_request = 0
    # 좀더 최적화 할수 있는데 굳이 그러고 싶지않음
    # 최적화함 4.002~5.001 을 1초로 하니 첫번째 조건문
    # start + 1000 > end 인 경우를 생각해서 2번째 조건문도 넣어줌
    while time <= time_end - 999 or time <= L[-1][0]:
        # 로그가 하나인 경우를 위해 빈큐가 아닌 1번째 원소가 들어간 큐로 초기화
        # re+1 < len(L)을 확인할 필요가 없는 이유는  time <= time_end에서 걸러지기 때문이다.
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
# L = [
# "2016-09-15 00:00:01.000 0.9s",
# "2016-09-15 00:00:02.000 0.9s",
# "2016-09-15 00:00:03.000 0.9s",
# "2016-09-15 00:00:04.000 2.999s",
#     ]
print(solution(L))