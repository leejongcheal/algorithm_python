def check(Map):
    global N, T
    steps = [(1,0),(-1,0),(0,1),(0,-1)]
    for tx, ty in T:
        for dx, dy in steps:
            x, y = tx + dx, ty + dy
            while 0 <= x < N and 0 <= y < N:
                if Map[x][y] == "O":
                    break
                if Map[x][y] == "S":
                    return 0
                x, y = x + dx, y + dy
    return 1

def dfs(x, y):
    global L, N, flag, count

    if flag == 1:
        return
    if count == 3:
        if check(L):
            flag = 1
        return
    for i in range(N):
        for j in range(N):
            if x < i or (j > y and x == i):
                if L[i][j] == "X":
                    L[i][j] = "O"
                    count += 1
                    dfs(i, j)
                    L[i][j] = "X"
                    count -= 1
    return

N = int(input())
L = [list(input().split()) for _ in range(N)]
T = []
flag = 0
count = 0
for i in range(N):
    for j in range(N):
        if L[i][j] == "T":
            T.append((i,j))
dfs(-1, -1)
if flag == 1:
    print("YES")
else:
    print("NO")