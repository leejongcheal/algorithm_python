from collections import  deque
def BFS(graph, wall, N , M):
    steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for w in wall:
        x, y = w[0], w[1]
        graph[x][y] = 1
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                q = deque()
                q.append((i,j))
                while q:
                    x ,y = q.popleft()
                    for step in steps:
                        nx = x + step[0]
                        ny = y + step[1]
                        if 0 <= nx < N and 0 <= ny < M:
                            if graph[nx][ny] == 0:
                                graph[nx][ny] = 3
                                q.append((nx, ny))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    return cnt

def comb(L, n):
    ret = []
    N = len(L)
    if len(L) < n:
        return None
    if n == 1:
        for i in L:
            ret.append([i])
    else:
        for i in range(N - n + 1):
            for temp in comb(L[i+1:], n-1):
                ret.append([L[i]] + temp)
    return ret


N, M = map(int, input().split())
result = 0
graph = []
#빈칸
blank = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            blank.append((i,j))
com_3_wall = comb(blank, 3)
g = [[0]*M for _ in range(N)]
for wall in com_3_wall:
    for i in range(N):
        for j in range(M):
            g[i][j] = graph[i][j]
    result = max(BFS(g, wall, N, M), result)
print(result)


