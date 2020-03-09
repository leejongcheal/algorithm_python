# DFS 는 생각할게 많은거 같음 BFS으로 풀어보자
from collections import deque


def check_location(x, y):
    global n, m
    if (0 <= x < n) and 0 <= y < m:
        return 1
    else:
        return 0


T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    L = []
    visit = []
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    final_time = 0
    for i in range(n):
        L.append(list(map(int, input().split())))
    y, x = map(int, input().split())
    x -= 1
    y -= 1
    L[x][y] = 2
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in dir:
            if check_location(x + i[0], y + i[1]) == 1 and L[x + i[0]][y + i[1]] == 1:
                L[x + i[0]][y + i[1]] = L[x][y] + 1
                q.append((x + i[0], y + i[1]))
        final_time = max(final_time, L[x][y])
    # for i in L:
    #     print(i)
    print(final_time-1)
