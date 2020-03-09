import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
N, M = map(int, input().split())
nameList = sys.stdin.read().splitlines()
L = []
for idx in range(N):
    a = []
    for c in nameList[idx]:
        a.append(int(c))
    L.append(a)
L[0][0] = 2
q = deque()
q.append((0, 0))
while q:
    i,j = q.popleft()
    if i == N - 1 and j == M - 1:
        print(L[i][j] - 1)
        exit()
    for m in range(4):
        x = i + dx[m]
        y = j + dy[m]
        if 0 <= x < N and 0 <= y < M and L[x][y] == 1:
                L[x][y] = L[i][j] + 1
                q.append((x, y))
