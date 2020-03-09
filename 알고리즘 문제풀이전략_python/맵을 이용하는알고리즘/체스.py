# BFS 풀이
from collections import deque


def check_location(x, y):
    global n, m
    if 0 <= x < n and 0 <= y < m:
        return 1
    else:
        return 0


T = int(input())
dir = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-1, -2), (-2, -1)]
for _ in range(T):
    n, m = map(int, input().split())
    visit = []
    for i in range(n):
        visit.append([0] * m)
    srcx, srcy, desx, desy = map(int, input().split())
    srcx -= 1
    srcy -= 1
    desx -= 1
    desy -= 1
    q = deque()
    q.append((srcx, srcy, 0))
    visit[srcx][srcy] = 1
    while q:
        i, j, r = q.popleft()
        if i == desx and desy == j:
            print(r)
            break
        for x, y in dir:
            if check_location(x + i, y + j) == 1 and visit[x + i][y + j] == 0:
                visit[x + i][y + j] = 1
                q.append((x + i, y + j, r + 1))
