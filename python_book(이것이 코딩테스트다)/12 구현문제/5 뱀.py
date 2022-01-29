from collections import deque
steps = [(0,1),(1,0),(0,-1),(-1,0)]
N = int(input())
Map = [[0]*N for _ in range(N)]
K = int(input())
for _ in range(K):
    i, j = map(int,input().split())
    Map[i-1][j-1] = 1
C = int(input())
bam = deque()
command = deque()
for _ in range(C):
    x, c = input().split()
    x = int(x)
    if c == "D":
        command.append((x,1))
    elif c == "L":
        command.append((x, -1))
x, y = (0, 0)
Map[0][0] = 2
d = 0
bam.append((0,0))
time = 0
flag = 1
if command:
    ntime, nd = command.popleft()
while 1:
    time += 1
    nx, ny = x + steps[d][0], y + steps[d][1]
    if 0 <= nx < N and 0 <= ny < N:
        if Map[nx][ny] == 0:
            tx, ty = bam.popleft()
            Map[tx][ty] = 0
            bam.append((nx, ny))
        elif Map[nx][ny] == 1:
            bam.append((nx, ny))
        elif Map[nx][ny] == 2:
            flag = 0
        x, y = nx, ny
        Map[x][y] = 2
    else:
        flag = 0
    if flag == 0:
        break
    if time == ntime:
        d += nd
        if command:
            ntime, nd = command.popleft()
print(time)