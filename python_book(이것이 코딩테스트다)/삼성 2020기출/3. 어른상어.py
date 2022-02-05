steps = [(-1, 0),(1, 0),(0, -1),(0, 1)]
N, M, K = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
D = list(map(int, input().split()))
for i in range(len(D)):
    D[i] -= 1
D_score = [[] for _ in range(M)]
for i in range(M):
    for j in range(4):
        D_score[i].append(list(map(int, input().split())))
shark_now = []
L = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        L[i][j] = [0,0]
        if Map[i][j] > 0:
            shark_now.append((Map[i][j],i,j))
            L[i][j] = [Map[i][j], K]
# L [index, 남은 k]
time = 0
while len(shark_now) > 1:
    # time > 1000 은 틀림 넘으면이면서 이상으로 해놓으면 어쩌라는거임
    if time >= 1000:
        time = -1
        break
    time += 1
    after_shark = [] # (인덱스, i, j) 순으로 저장 # 방향은 D에다 저장할것
    # 상어 위치 구하기
    for shark_index, x, y in shark_now:
        d = D[shark_index - 1]
        decode_d = D_score[shark_index - 1][d]
        flag = 0
        for di in range(4):
            nd = decode_d[di] - 1
            dx, dy = steps[nd]
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if L[nx][ny][0] == 0: #or L[nx][ny][0] == shark_index:
                    after_shark.append((shark_index,nx,ny))
                    D[shark_index - 1] = nd
                    flag = 1
                    break
        if flag == 0:
            for di in range(4):
                nd = decode_d[di] - 1
                dx, dy = steps[nd]
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if L[nx][ny][0] == shark_index:
                        after_shark.append((shark_index,nx,ny))
                        D[shark_index - 1] = nd
                        break
    # k -= 1 해주기
    for i in range(N):
        for j in range(N):
            if L[i][j][0] != 0:
                L[i][j][1] -= 1
                if L[i][j][1] == 0:
                    L[i][j][0] = 0
    # 구한 상어값 넣어주기
    after_shark.sort()
    shark_now = []
    for shark_index, x, y in after_shark:
        if L[x][y][0] == 0:
            L[x][y][0] = shark_index
            L[x][y][1] = K
            shark_now.append((shark_index, x, y))
        elif L[x][y][0] == shark_index:
            L[x][y][0] = shark_index
            L[x][y][1] = K
            shark_now.append((shark_index, x, y))
        elif L[x][y][0] < shark_index:
            continue
print(time)