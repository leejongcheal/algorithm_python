def DFS(v):
    global fare, final, L, visit, n
    visit[v] = 1
    if fare > final:
        visit[v] = 0
        return
    if visit.count(0) == 0:
        final = min(final, fare)
        visit[v] = 0
        return
    for i in range(n):
        if visit[i] == 0:
            fare += L[v][i]
            DFS(i)
            fare -= L[v][i]
    visit[v] = 0


T = int(input())
for _ in range(T):
    n = int(input())
    final = 100000000
    fare = 0
    L = []
    visit = [0]*n
    for i in range(n):
        L.append(list(map(int, input().split())))
    for i in range(n):
        DFS(i)
    print(final)
