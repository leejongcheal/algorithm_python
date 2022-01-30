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

def dfs(count):
    global Map, N, flag
    if flag == 1:
        return
    if count == 3:
        if check(Map):
            flag = 1
    else:
        for i in range(N):
            for j in range(N):
                if Map[i][j] == "X":
                    Map[i][j] = "O"
                    dfs(count + 1)
                    Map[i][j] = "X"



N = int(input())
Map = [list(input().split()) for _ in range(N)]
T = []
for i in range(N):
    for j in range(N):
        if Map[i][j] == "T":
            T.append((i,j))
# flag = 1 이면 가능하다는 뜻
flag = 0
dfs(0)
if flag == 1:
    print("YES")
else:
    print("NO")
