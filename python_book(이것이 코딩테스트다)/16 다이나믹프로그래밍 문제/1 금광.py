def solution(Map, N, M):
    DP = [[0]*M for _ in range(N)]
    for i in range(N):
        DP[i][0] = Map[i][0]
    for j in range(1, M):
        for i in range(N):
            if 0 <= i - 1 < N:
                DP[i][j] = max(DP[i][j], DP[i-1][j-1] + Map[i][j])
            if 0 <= i + 1 < N:
                DP[i][j] = max(DP[i][j], DP[i+1][j-1] + Map[i][j])
            DP[i][j] = max(DP[i][j], DP[i][j-1] + Map[i][j])
    Max = 0
    for i in range(N):
        Max = max(DP[i][M-1], Max)
    return Max


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    L = list(map(int ,input().split()))
    Map = [[0]*M for _ in range(N)]
    index = 0
    for i in range(N):
        for j in range(M):
            Map[i][j] = L[index]
            index += 1
    print(solution(Map,  N, M))

"""
예시 인풋
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4 
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""