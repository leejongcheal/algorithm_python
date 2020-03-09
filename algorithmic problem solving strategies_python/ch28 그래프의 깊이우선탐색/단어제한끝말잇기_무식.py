def dfs(c):
    global L, res, n
    res.append(c)
    if len(res) == n:
        return 1
    for dc in L:
        if dc not in res:
            if c[-1] == dc[0]:
                dfs(dc)
    res = res[0:-1]


T = int(input())
for _ in range(T):
    flag = 0
    n = int(input())
    L = []
    for _ in range(n):
        L.append(input())
    print(L)
    res = []
    for c in L:
        if dfs(c) == 1:
            flag = 1
            for r in res:
                print(r,end =" ")
            break
    if flag == 0:
        print("Impossible", end=" ")
    print()

