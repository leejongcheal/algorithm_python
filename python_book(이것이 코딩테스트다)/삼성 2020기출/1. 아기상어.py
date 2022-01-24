from collections import deque

steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def sizing(size, now_index):
    if size == now_index:
        size += 1
        now_index = 0
    return size, now_index


#  이동 가능 -> time 까지 계산 + 1리턴 // 못움직이면 0 리턴
def BFS(L, size, sx, sy):
    global N, time
    visit = [[-1]*N for _ in range(N)]
    visit[sx][sy] = 0
    q = deque()
    q.append((sx,sy))
    while q:
        x, y = q.popleft()
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == -1 and L[nx][ny] <= size:
                q.append((nx, ny))
                visit[nx][ny] = visit[x][y] + 1
    min = int(1e9)
    min_index = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] > 0 and 0 < L[i][j] < size:
                if visit[i][j] < min:
                    min = visit[i][j]
                    min_index = (i, j)
    if min_index != 0:
        time += min
        x, y = min_index
        L[sx][sy] = 0
        L[x][y] = 9
        return x, y
    else:
        return 0



N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
# 현재 위치 sx sy 로 두기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            sx, sy = i, j
size = 2
now_index = 0
time = 0
while 1:
    a = BFS(graph, size, sx, sy)
    if a == 0:
        break
    else:
        sx, sy = a
    size, now_index = sizing(size, now_index + 1)
print(time)