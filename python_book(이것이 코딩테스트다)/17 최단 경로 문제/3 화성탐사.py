import heapq
INF = int(1e9)
T = int(input())
steps = [(1,0), (-1,0),(0,1),(0,-1)]
for _ in range(T):
    N = int(input())
    Map = []
    res = []
    res = [[INF]*N for c in range(N)]
    for i in range(N):
        Map.append(list(map(int, input().split())))
    q = []
    res[0][0] = Map[0][0]
    heapq.heappush(q,(res[0][0],0,0))
    while q:
        value, x, y = heapq.heappop(q)
        if value > res[x][y]:
            # print(3)
            continue
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]
            if 0<= nx < N and 0 <= ny < N:
                # print(1)
                dist = value + Map[nx][ny]
                if res[nx][ny] > dist:
                    # print(2)
                    res[nx][ny] = dist
                    heapq.heappush(q,(dist, nx, ny))
    # for r in res:
    #     print(r)
    print(res[N-1][N-1])



