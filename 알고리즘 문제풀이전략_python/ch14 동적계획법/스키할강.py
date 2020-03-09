def solve(L, n):
    for i in range(n-1, 0, -1):
        for j in range(i):
            L[i-1][j] += max(L[i][j], L[i][j+1])
    print(L[0][0])


T = int(input())
for _ in range(T):
    n = int(input())
    L = []
    for i in range(n):
        L.append(list(map(int, input().split())))
    solve(L, n)
