import sys
from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
input = sys.stdin.readline
t = int(input())
for idx in range(t):
    n = int(input())
    v = [[0] * n for _ in range(n)]
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    end = 0
    q = deque()
    v[a][b] = 1
    q.append((a, b))
    if a == c and b == d:
        print(0)
        continue
    while q:
        x, y = q.popleft()
        for i in range(8):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n and v[x + dx[i]][y + dy[i]] == 0:
                if x + dx[i] == c and y + dy[i] == d:
                    print(v[x][y])
                    end = 1
                    break
                v[x + dx[i]][y + dy[i]] = v[x][y] + 1
                q.append((x + dx[i], y + dy[i]))
        if end == 1:
            break
