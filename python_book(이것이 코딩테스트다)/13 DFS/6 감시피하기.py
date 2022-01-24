steps = [(1,0),(-1,0),(0,1),(0,-1)]
def check(T_list, Map):
    global N
    for x, y in T_list:
        for dx, dy in steps:
            for i in range(1,N):
                nx, ny = x + dx*i, y + dy*i
                if 0 <= nx < N and 0 <= ny < N:
                    if Map[nx][ny] == "S":
                        return 0
                    elif Map[nx][ny] == "O":
                        break
                else:
                    break
    return 1


def comb(L, N):
    length = len(L)
    if length < N:
        return ""
    ret = []
    if N == 1:
        for l in L:
            ret.append([l])
    else:
        for i in range(length - N + 1):
            for temp in comb(L[i+1:], N-1):
                ret.append([L[i]] + temp)
    return ret


N = int(input())
Map = []
for _ in range(N):
    Map.append(list(input().split()))
X_list = []
T_list = []
for i in range(N):
    for j in range(N):
        if Map[i][j] == "T":
            T_list.append((i, j))
        if Map[i][j] == "X":
            X_list.append((i,j))
flag = 0
for O_list in comb(X_list, 3):
    if flag == 1:
        break
    for i in range(3):
        x, y = O_list[i]
        Map[x][y] = "O"
    if check(T_list, Map):
        flag = 1
        break
    for i in range(3):
        x, y = O_list[i]
        Map[x][y] = "X"
if flag == 1:
    print("YES")
else:
    print("NO")