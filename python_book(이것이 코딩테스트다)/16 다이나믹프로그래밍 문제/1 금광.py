def solution(result, x, y):
    global Map, N, M
    if result[x][y] != -1:
        return result[x][y]
    if y == 0:
        result[x][y] = Map[x][y]
    else:
        if x == 0:
            result[x][y] = max(solution(result, x, y - 1), solution(result, x + 1, y - 1)) + Map[x][y]
        elif x == N - 1:
            result[x][y] = max(solution(result, x - 1, y - 1), solution(result, x, y - 1)) + Map[x][y]
        else:
            result[x][y] = max(solution(result, x - 1, y - 1), solution(result, x, y - 1),
                               solution(result, x + 1, y - 1)) + Map[x][y]
    return result[x][y]


T = int(input())
for tc in range(T):
    N, M = map(int, input().rstrip().split())
    L = list(map(int, input().rstrip().split()))
    # print(L)
    Map = [[-1] * M for _ in range(N)]
    result = [[-1] * M for _ in range(N)]
    t = 0
    for i in range(N):
        for j in range(M):
            Map[i][j] = L[t]
            t += 1
    for i in range(N):
        solution(result, i, M - 1)
    max_value = -1
    for i in range(N):
        max_value = max(max_value, result[i][M-1] )
    print(max_value)