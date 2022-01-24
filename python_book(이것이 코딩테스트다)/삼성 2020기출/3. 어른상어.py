steps = [(-1,0),(1,0),(0,-1),(0,1)]

# 찾으면 해당 위치 없으면 0 리턴
def find_index(graph, n):
    global N, K
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0 and graph[i][j][0] == n and graph[i][j][2] == K:
                return (i, j)
    return 0


def move_shark(graph, x, y, n):
    global D_list
    d = graph[x][y][1]
    D = D_list[n-1][d]
    flag = 0
    # 빈공간
    for i in range(4):
        nd = D[i]
        nx, ny = x + steps[nd][0], y + steps[nd][1]
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
            return nx, ny, nd
    # 냄새로 가야하는 경우
    for i in range(4):
        nd = D[i]
        nx, ny = x + steps[nd][0], y + steps[nd][1]
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] != 0:
            if graph[nx][ny][0] == n:
                return nx, ny, nd


def move(graph):
    global N, M, K, shark_cnt
    shark_list = []
    for n in range(1, M+1):
        a = find_index(graph, n)
        if a != 0:
            x, y = a
            nx, ny, nd = move_shark(graph, x, y, n)
            shark_list.append((n, nx, ny, nd))
    #   K 수정후에 상어이동 해주기 -> 왜냐면 K가 1인경우 상어 부분도 -1해버려서 내용이 사라짐
    # 따라서 K를 먼저 -1 해주고 상어 이동해주면 깔끔함
    # 어쩌피 상어는 빈공간 아니면 내냄새로 가기 떄문에 나의 냄새부분이 빈공간으로 바껴도 논리적으로 아무런
    # 상관없음을 인지
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                graph[i][j][2] -= 1
                if graph[i][j][2] == 0:
                    graph[i][j] = 0
    #  shrak_list 내용 토대로 데이터 갱신
    # 번호가 다른곳으로 들어가는 경우에 sh_cnt -= 1하고 무시
    for s in shark_list:
        n, sx, sy, sd = s
        # 빈공간인 경우
        if graph[sx][sy] == 0:
            graph[sx][sy] = [n, sd, K]
        # 빈공간이 아닌 경우
        else:
            # 내냄새인 경우
            if graph[sx][sy][0] == n:
                graph[sx][sy] = [n, sd, K]
            # 다른 상어 있는 경우 무조건 작은넘버가 들어가 있다고 가정
            else:
                shark_cnt -= 1



N, M, K = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
D = list(map(int, input().split()))
for i in range(M):
    D[i] -= 1
D_list = []
for i in range(M):
    D_l = []
    for j in range(4):
        D_l.append(list(map(int, input().split())))
    D_list.append(D_l)
for i in range(M):
    for j in range(4):
        for x in range(4):
            D_list[i][j][x] -= 1
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            n = graph[i][j]
            d = D[n-1]
            k = K
            graph[i][j] = [n, d, k]
# 입력 및 데이터처리 끝
shark_cnt = M
time = 0
# shark_cnt 는 전역변수 처리
while shark_cnt > 1:
    time += 1
    if time > 1000:
        time = -1
        break
    move(graph)
# for i in range(5):
#     print(i+1)
#     move(graph)
#     for g in graph:
#         print(g)
print(time)