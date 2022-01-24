from collections import deque

steps = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


def fish_move(L, x, y):
    d = L[x][y * 2 + 1]
    for i in range(8):
        nd = (d + i)%8
        nx, ny = x + steps[nd][0], y + steps[nd][1]
        # 이동 가능한경우
        if 0 <= nx < 4 and 0 <= ny < 4 and L[nx][2 * ny] != -1:
            d = nd
            L[x][2 * y], L[nx][ny * 2] = L[nx][ny * 2], L[x][y * 2]
            L[x][2 * y + 1], L[nx][ny * 2 + 1] = L[nx][ny * 2 + 1], d
            break


def find_index(L, n):
    for i in range(4):
        for j in range(4):
            if L[i][2 * j] == n:
                return (i, j)
    return 0


# 상어 -1 ++ 값과 방향 둘다 이동
def fish_all_move(L):
    for n in range(1, 17):
        a = find_index(L, n)
        if a != 0:
            x, y = a
            fish_move(L, x, y)


def deep_copy(L):
    C = [[-1] * 8 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            C[i][2 * j], C[i][j * 2 + 1] = L[i][2 * j], L[i][2 * j + 1]
    return C


def BFS(L, res_list):
    q = deque()
    res = L[0][0]
    L[0][0] = -1
    sx, sy = 0, 0
    q.append((L, sx, sy, res))
    while q:
        L, sx, sy, res = q.popleft()
        fish_all_move(L)
        x, y = sx, sy
        d = L[x][y*2 +1]
        flag = 0
        for i in range(4):
            nx, ny = x + i*(steps[d][0]), y + i*(steps[d][1])
            if 0 <= nx < 4 and 0 <= ny < 4:
                if L[nx][ny*2] > 0:
                    fish_number = L[nx][ny*2]
                    C = deep_copy(L)
                    C[sx][sy*2] = 0
                    C[nx][ny*2] = -1
                    q.append((C,nx, ny, res + fish_number))
                    flag = 1
            else:
                break
        if flag == 0:
            res_list.append(res)

# 입력및 수정
graph = []
for _ in range(4):
    graph.append(list(map(int, input().split())))
for i in range(4):
    for j in range(4):
        graph[i][2 * j + 1] -= 1
# 상어 -1, 빈공간 0 나머지는 물고기 고유번호
res_list = []
BFS(graph, res_list)
print(max(res_list))