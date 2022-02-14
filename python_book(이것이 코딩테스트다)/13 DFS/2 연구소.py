from typing import List
from copy import deepcopy
def count(L: List):
    sum = 0
    for i in range(N):
        for j in range(M):
            if L[i][j] == 0:
                sum += 1
    return sum

def fill_dfs(L:List, x, y):
    steps = [(1,0),(-1,0),(0,-1),(0,1)]
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and L[nx][ny] == 0:
            L[nx][ny] = 2
            fill_dfs(L, nx, ny)
def dfs_3(x, y, k, prev_index: List = []):
    global res
    if k == 3:
        # 일단 이 visit을 안쓴경우에 더 빨랐는데 말이안됨 사실
        # -> 전의 벽보다 큰값만 벽치게해도 3개든 4개든 겹치는 경우 없어짐
        # prev_index에 대해서 정렬할 필요없이 알아서 순서대로 들어가게 코딩함
        if tuple(prev_index) not in set_visit:
            copy = deepcopy(L)
            for vx, vy in virus:
                fill_dfs(copy, vx, vy)
            # 이런식으로 정렬할 필요가 없음
            # set_visit.add(tuple(sorted(prev_index)))
            set_visit.add(tuple(prev_index))
            res = max(res, count(copy))
        else:
            # 확인 결과 상관없음 + 어쩌피 출력안하니 놓아도됨 ㅋㅋ
            print("3개의벽이 중복되는 경우에 출력 -> 백준결과 출력안함")
        return
    for i in range(x, N):
        for j in range(M):
            if i == x and j < y:
                continue
            if L[i][j] == 0:
                L[i][j] = 1
                dfs_3(i, j, k + 1, prev_index + [(i, j)])
                L[i][j] = 0

N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
virus = []
for i in range(N):
    for j in range(M):
        if L[i][j] == 2:
            virus.append((i, j))
set_visit = set()
res = 0
dfs_3(0,0,0)
print(res)

