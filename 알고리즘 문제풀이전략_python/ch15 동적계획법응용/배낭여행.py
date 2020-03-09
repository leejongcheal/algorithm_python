def DFS(v, r):
    global n
    global res
    global L
    if len(v) == n:
        if L[v[-1]][0] != 0:
            # print(v)
            res.append(r + L[v[-1]][0])
        return
    for i in range(1, n):
        if i in v:
            continue
        if L[v[-1]][i] != 0:
            l = v.copy()
            l.append(i)
            DFS(l, r + L[v[-1]][i])


T = int(input())
for _ in range(T):
    n = int(input())
    L = []
    for i in range(n):
        L.append(list(map(int, input().split())))
    v = [0]
    r = 0
    res = []
    DFS(v, r)
    # print(res)
    print(min(res))
