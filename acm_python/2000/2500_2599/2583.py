import sys
sys.setrecursionlimit(100000)


def fill(x, y, x1, y1):
    global L
    for i in range(x, x1):
        for j in range(y, y1):
            L[j][i] = 1


def DFS(x, y):
    global s
    s += 1
    if x + 1 < n and v[x + 1][y] == 0 and L[x + 1][y] == 0:
        v[x + 1][y] = 1
        DFS(x + 1, y)
    if x - 1 >= 0 and v[x - 1][y] == 0 and L[x - 1][y] == 0:
        v[x - 1][y] = 1
        DFS(x - 1, y)
    if y - 1 >= 0 and v[x][y - 1] == 0 and L[x][y - 1] == 0:
        v[x][y - 1] = 1
        DFS(x, y - 1)
    if y + 1 < m and v[x][y + 1] == 0 and L[x][y + 1] == 0:
        v[x][y + 1] = 1
        DFS(x, y + 1)


n, m, k = map(int, input().split())
L = [[0] * m for _ in range(n)]
v = [[0] * m for _ in range(n)]
for _ in range(k):  # 1로 채워주기
    x, y, x1, y1 = map(int, input().split())
    fill(x, y, x1, y1)
res = []
num = 0
for i in range(n):
    for j in range(m):
        if L[i][j] == 0 and v[i][j] == 0:
            num += 1
            v[i][j] = 1
            s = 0
            DFS(i, j)
            res.append(s)
print(num)
for item in sorted(res):
    print(item, end=" ")
