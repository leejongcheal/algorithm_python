import sys
from collections import deque


def BFS(x, y):
    v = [[0] * m for _ in range(n)]
    q = deque()
    v[x][y] = 1
    q.append((x, y))
    while q:
        x, y = q.popleft()
        if x + 1 < n and L[x + 1][y] == "L" and v[x + 1][y] == 0:
            v[x + 1][y] = v[x][y] + 1
            q.append((x + 1, y))
        if x - 1 >= 0 and L[x - 1][y] == "L" and v[x - 1][y] == 0:
            v[x - 1][y] = v[x][y] + 1
            q.append((x - 1, y))
        if y + 1 < m and L[x][y + 1] == "L" and v[x][y + 1] == 0:
            v[x][y + 1] = v[x][y] + 1
            q.append((x, y + 1))
        if y - 1 >= 0 and L[x][y - 1] == "L" and v[x][y - 1] == 0:
            v[x][y - 1] = v[x][y] + 1
            q.append((x, y - 1))
    return v[x][y]-1


n, m = map(int, input().split())
L = [input() for _ in range(n)]
res = 0
for i in range(n):
    for j in range(m):
        if L[i][j] == "L":
            res = max(res, BFS(i, j))
print(res)
