import sys
sys.setrecursionlimit(10**8)


def DFS(i,j):
    if i+1 < n and v[i+1][j] == 0 and L[i+1][j] == L[i][j]:
        v[i+1][j] = 1
        DFS(i+1,j)
    if i-1 >= 0 and v[i-1][j] == 0 and L[i-1][j] == L[i][j]:
        v[i-1][j] = 1
        DFS(i-1,j)
    if j+1 < n and v[i][j+1] == 0 and L[i][j+1] == L[i][j]:
        v[i][j+1] = 1
        DFS(i,j+1)
    if j-1 >= 0 and v[i][j-1] == 0 and L[i][j-1] == L[i][j]:
        v[i][j-1] = 1
        DFS(i,j-1)

n = int(input())
L = [list(s) for s in sys.stdin.read().splitlines()]
v = [[0]*n for _ in range(n)]
a,b = 0,0
for i in range(n):
    for j in range(n):
        if v[i][j] == 0:
            a += 1
            DFS(i,j)
v = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if L[i][j] == "G":
            L[i][j] = "R"
for i in range(n):
    for j in range(n):
        if v[i][j] == 0:
            b += 1
            DFS(i,j)
print(a,b)
