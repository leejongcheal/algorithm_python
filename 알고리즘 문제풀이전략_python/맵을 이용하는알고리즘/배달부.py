# DFS로 풀이
def DFS(src):
    global visit, dist, map, final, n
    visit[src] = 1
    if visit.count(0) == 0:
        if src == n-1:
            final = min(dist,final)
        visit[src] = 0
    for i in range(n):
        if visit[i] == 0 and map[src][i] != 0:
            dist += map[src][i]
            DFS(i)
            dist -= map[src][i]
    visit[src] = 0


T = int(input())
for _ in range(T):
    t, n = map(int, input().split())
    map = []
    visit = [0]*n
    final = 10000000
    dist = 0
    for i in range(n):
        map.append([0] * n)
    for a in range(t):
        L = list(input().split())
        i, j ,m = int(L[0]),int(L[1]),int(L[2])
        if map[i-1][j-1] == 0:
            map[i-1][j-1] = map[j-1][i-1] = m
        else:
            map[i-1][j-1] = map[j-1][i-1] = min(m, map[i-1][j-1])
    DFS(0)
    print(final)
