import heapq


def solution(L, N):
    steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    INF = int(1e10)
    dij = [[INF]*N for _ in range(N)]
    q = []
    dij[0][0] = L[0][0]
    heapq.heappush(q, (L[0][0], 0, 0))
    while q:
        dist, x, y = heapq.heappop(q)
        if dij[x][y] < dist:
            continue
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if dij[nx][ny] > dist + L[nx][ny]:
                    dij[nx][ny] = dist + L[nx][ny]
                    heapq.heappush(q, (dij[nx][ny], nx, ny))
    return dij[N - 1][N - 1]


T = int(input())
for tc in range(T):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    print(solution(L, N))