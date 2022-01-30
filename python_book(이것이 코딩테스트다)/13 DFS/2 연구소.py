from collections import deque


def comb(L, M):
    N = len(L)
    if N < M:
        return None
    res = []
    if M == 1:
        for l in L:
            res.append([l])
    else:
        for i in range(N - M + 1):
            for temp in comb(L[i + 1:], M - 1):
                res.append([L[i]] + temp)
    return res


# visit을 안써도 0인 부분에 대해서 검사를  하기떄문에 상관없을듯? 크기도 작고
# 확인필요 -> 안해도 상관없음
def BFS(Map, x, y):
    q = deque()
    q.append((x, y))
    global steps, N, M
    while q:
        x, y = q.popleft()
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if Map[nx][ny] == 0:
                    q.append((nx, ny))
                    Map[nx][ny] = 2


def check(Map):
    global N, M
    cnt = 0
    for i in range(N):
        for j in range(M):
            if Map[i][j] == 0:
                cnt += 1
    return cnt


def copy_list(Map):
    global N, M
    # copy_Map을 굳이 계속 새로만들 필요없이 한번만 초기화해주고 Map값을 넣어줘서 사용
    # 하면 메모리 아낄수 있음
    # copy_list(Map, copy_Map)으로 두고 메인에서 한번만 copy_Map 초기화
    copy_Map = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            copy_Map[i][j] = Map[i][j]
    return copy_Map


steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
virus = []
blank = []
res = 0
for i in range(N):
    for j in range(M):
        if Map[i][j] == 2:
            virus.append([i, j])
        elif Map[i][j] == 0:
            blank.append([i, j])
for blank_3 in comb(blank, 3):
    copy_Map = copy_list(Map)
    for b in blank_3:
        x, y = b[0], b[1]
        copy_Map[x][y] = 1
    for v in virus:
        x, y = v[0], v[1]
        BFS(copy_Map, x, y)
    res = max(res, check(copy_Map))
print(res)
