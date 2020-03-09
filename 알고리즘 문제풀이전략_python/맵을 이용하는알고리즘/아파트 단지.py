# DFS로 풀어보자 일부로!
import sys
sys.setrecursionlimit(10 ** 8)


def check_location(x, y):
    global n
    if 0 <= x < n and 0 <= y < n:
        return 1
    else:
        return 0


def DFS(i, j):
    global visit, L, dir
    visit[i][j] = 1
    for x, y in dir:
        if check_location(i + x, y + j) == 1:
            if L[i + x][j + y] == 1 and visit[i + x][j + y] == 0:
                # print(i+x,y+j)
                DFS(i + x, j + y)


T = int(input())
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for _ in range(T):
    n = int(input())
    L = []
    visit = []
    for i in range(n):
        L.append(list(map(int, input().split())))
        visit.append([0] * n)
    solution = 0
    for i in range(n):
        for j in range(n):
            if L[i][j] == 1 and visit[i][j] == 0:
                solution += 1
                DFS(i, j)
    print(solution)
