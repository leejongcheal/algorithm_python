# 최적화 문제로 문제가 매우매우 훌룡해서 따로 풀어보기로함
# 모든 도시를 방문하는 거리의 최소값 찾기
# 0을 방문하기는 하지만 0이 시작점인 경로가 최소인건 아니다 ....
# cpp 는 통과하는데 파이썬은 통과못함 ㅅㅂ 이래서 acm으로 가지 알고스팟 ㅎㅌㅊ
import sys
from collections import deque


def short(path, currentLength):
    global dist, n
    if len(path) == n:
        return currentLength
    ret = 10000000000000
    for i in range(n):
        if i in path:
            continue
        here = path[-1]
        path.append(i)
        cand = short(path,currentLength + dist[here][i])
        ret = min(ret,cand)
        path.pop()
    return ret


T = int(input())
read = sys.stdin.readline
for _ in range(T):
    dist = []
    n = int(read())
    for _ in range(n):
        dist.append(list(map(float, read().split())))
    path = deque()
    ret = 10000000
    for i in range(n):
        path.append(i)
        ret = min(short(path,0),ret)
        path.pop()
    print("%.10f"%ret)
