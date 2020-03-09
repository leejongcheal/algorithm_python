import sys
from collections import deque
n, m = map(int,input().split())
L = sys.stdin.read().splitlines()
v = [[0]*(n+1) for _ in range(n+1)]
for idx in range(m):
    a,b = map(int,L[idx].split())
    v[a][b] = 1
    v[b][a] = 1
r = 0
for i in range(1,n+1):
    if v[i][i] == 0:
        r += 1
        q =deque()
        q.append(i)
        v[i][i] = 2
        while q:
            x = q.popleft()
            for y in range(1,n+1):
                if v[x][y] == 1 and v[y][y] == 0:
                    v[y][y] = 2
                    q.append(y)
print(r)
