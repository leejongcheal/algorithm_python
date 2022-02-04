from collections import deque
def cal_distance(now_shark):
    global N, L, visit, now_size
    steps = [(-1,0),(0,-1),(1,0),(0,1)]
    for i in range(N):
        for j in range(N):
            visit[i][j] = 0
    x, y = shark_now
    min_dist = int(1e10)
    min_list = []
    visit[x][y] = 1
    q = deque()
    q.append((x,y,0))
    """
    q에 dist를 넣는대신 visit을 -1로 초기화 하고 현재위치를 0으로 둔다
    그다음에 방문하는거에 대해서 visit[nx][ny] = visit[x][y] + 1로 두면 visit에 dist값을 저장할수 있음 
    """
    while q:
        x, y, dist = q.popleft()
        # 처음으로 먹을수 있는 물고기를 찾은경우
        if L[x][y] < now_size and 1 <= L[x][y] <= 6 and dist < min_dist:
            min_dist = dist
            min_list = [(x, y)]
        # 물고기를 먹는데 같은 거리가 있는 경우
        elif L[x][y] < now_size and 1 <= L[x][y] <= 6 and dist == min_dist:
            min_list.append((x, y))
        # 최소거리보다큰 먹을수 있는 물고기의 경우는 필요없으니 break
        elif dist > min_dist:
            break
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
                if L[nx][ny] <= now_size:
                    visit[nx][ny] = 1
                    q.append((nx, ny, dist + 1))
    return min_list, min_dist


N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*N for _ in range(N)]
shark_now = (0,0)
now_size = 2
now_fish = 0
for i in range(N):
    for j in range(N):
        if L[i][j] == 9:
            shark_now = (i, j)
            break
time = 0
while 1:
    min_list, min_dist = cal_distance(shark_now)
    if len(min_list) == 0:
        break
    else:
        min_list.sort()
        x, y = min_list[0]
        nx, ny = shark_now
        L[nx][ny] = 0
        L[x][y] = 9
        now_fish += 1
        if now_fish == now_size:
            now_size += 1
            now_fish = 0
        time += min_dist
        shark_now = (x, y)
print(time)

