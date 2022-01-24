from collections import deque


steps = [(-1, 0),(0, 1),(1, 0),(0, -1)]
def solution(Map, D, N):
    d = 1
    q = deque()
    q.append((0,0))
    bam = (0,0)
    t = 0
    while 1:
        t += 1
        x, y = bam
        nx, ny = x + steps[d][0], y + steps[d][1]
        if 0 <= nx < N and 0 <= ny < N:
            if Map[nx][ny] == 0:
                Map[nx][ny] = 1
                q.append((nx,ny))
                tx, ty = q.popleft()
                Map[tx][ty] = 0
            elif Map[nx][ny] == 2:
                Map[nx][ny] = 1
                q.append((nx,ny))
            elif Map[nx][ny] == 1:
                return t
            bam = (nx, ny)
        else:
            return t
        d = (d + D[t])%4


N = int(input())
Map = [[0]*N for _ in range(N)]
Map[0][0] = 1
K = int(input())
# -1 해서 사용 하기
for _ in range(K):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    Map[x][y] = 2
T = int(input())
D = [0]*(10001)
for _ in range(T):
    t, dir = input().split()
    t = int(t)
    if dir == "D":
        D[t] = 1
    elif dir == "L":
        D[t] = -1
print(solution(Map, D, N))