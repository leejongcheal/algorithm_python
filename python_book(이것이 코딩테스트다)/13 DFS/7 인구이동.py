from collections import deque
def BFS(x, y, graph, union_visit):
    global N, L, R
    # xy 포함된 연합찾고 연합값으로 그래프 업데이트
    # 만약에 연합이 있는 경우에 1 리턴 아니면 0리턴
    if union_visit[x][y] != 0:
        return 0
    start = (x, y)
    steps = [(1,0),(-1,0),(0,1),(0,-1)]
    union = [(x,y)]
    union_visit[x][y] = 1
    q = deque()
    q.append((x,y))
    total_value = graph[x][y]
    while q:
        x, y = q.popleft()
        for step in steps:
            nx, ny = x + step[0], y+step[1]
            if 0 <= nx < N and 0 <= ny < N and union_visit[nx][ny] == 0:
                if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                    q.append((nx,ny))
                    union_visit[nx][ny] = 1
                    union.append((nx,ny))
                    total_value += graph[nx][ny]
    if len(union) > 1:
        # print(total_value, len(union))
        union_avg = total_value // (len(union))
        for x, y in union:
            graph[x][y] = union_avg
        return 1
    else:
        # 어쩌피 방문해서 검사한경우 연합이 없는 좌표는 인접한 어떤점에 대해서 연합을 못만드는것이니 나중에 인접한 좌표에서 연합인지 검사할 필요가 없음
        # x, y = start
        # union_visit[x][y] = 0
        return 0

N, L, R = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
turn = 0
flag = 1
while 1:
    flag = 0
    union_visit = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if BFS(i,j, graph, union_visit) == 1:
                flag = 1
    if flag == 0:
        break
    turn += 1
print(turn)