import sys
n = int(input())
# nameList = sys.stdin.read().splitlines()
L = []
res = 1
max_length = 0
L = [[int(i) for i in input().split()] for _ in range(n)]
max_length = max([max(i) for i in L])
for length in range(1, max_length):
    res_bfs = 0
    v = [[0]*n for _ in range(n)]
    q = []
    for x in range(n):
        for y in range(n):
            if L[x][y] > length and v[x][y] == 0:
                res_bfs += 1
                q.append((x, y))
                v[x][y] = 1
                while q:
                    i, j = q.pop()
                    if i + 1 < n and L[i + 1][j] > length and v[i+1][j] == 0:
                        q.append((i + 1, j))
                        v[i+1][j] = 1
                    if i - 1 >= 0 and L[i - 1][j] > length and v[i-1][j] == 0:
                        q.append((i - 1, j))
                        v[i-1][j] = 1
                    if j - 1 >= 0 and L[i][j - 1] > length and v[i][j-1] == 0:
                        q.append((i, j - 1))
                        v[i][j-1] = 1
                    if j + 1 < n and L[i][j + 1] > length and v[i][j+1] == 0:
                        q.append((i, j + 1))
                        v[i][j+1] = 1
    res = max(res, res_bfs)
print(res)
