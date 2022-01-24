def BFS(graph, x, y, k):
    global N
    global black_cnt
    global plus_list
    steps = [(1,0),(-1,0),(0,1),(0,-1)]
    for step in steps:
        nx = x + step[0]
        ny = y + step[1]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 0:
                graph[nx][ny] = k
                plus_list.append((nx, ny))
                black_cnt -= 1


N, K = map(int, input().split())
virus_list = [[] for _ in range(K+1)]
graph = []
black_cnt = 0
for _ in range(N):
    graph.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            black_cnt += 1
        else:
            virus_list[graph[i][j]].append((i, j))
S, X, Y = map(int, input().split())
time = 0
# 종료조건 타임이 S초 또는 빈칸의 갯수 0개인경우
while 1:
    if time == S:
        break
    time += 1
    for i in range(1, K+1):
        plus_list = []
        for x, y in virus_list[i]:
            BFS(graph, x, y, i)
        virus_list[i].extend(plus_list)
    if black_cnt <= 0:
        break

print(graph[X-1][Y-1])


## 깔끔풀이
# N, K = map(int, input().split())
# graph = []
# virus = [[] for _ in range(K)]
# steps = [(1,0),(-1,0),(0,1),(0,-1)]
# for i in range(N):
#     graph.append(list(map(int, input().split())))
# S, X, Y = map(int, input().split())
# for i in range(N):
#     for j in range(N):
#         if graph[i][j] != 0:
#             virus[graph[i][j]-1].append((i,j))
# for i in range(S):
#     for v in range(K):
#         if len(virus[v]) != 0:
#             new = []
#             while virus[v]:
#                 x,y = virus[v].pop()
#                 for step in steps:
#                     nx = x + step[0]
#                     ny = y + step[1]
#                     if 0 <= nx < N and  0<= ny < N and graph[nx][ny] == 0:
#                         graph[nx][ny] = v+1
#                         new.append((x,y))
#             virus[v] = new
# print(graph[X-1][Y-1])