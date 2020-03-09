import sys
N = int(input())
nameList = sys.stdin.read().splitlines()
dx = {}
dy = {}
xcnt = 0
ycnt = 0
for idx in range(N):
    x, y = map(int, nameList[idx].split())
    dx[x] = dx.get(x, 0) + 1
    if dx[x] == 2:
        xcnt += 1
    dy[y] = dy.get(y, 0) + 1
    if dy[y] == 2:
        ycnt += 1
print(xcnt+ycnt)
