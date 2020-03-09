import sys
#from collections import deque
def make_water():
    global v
    global wq  # 전에 물로 바낀 부분만 검사
    w = wq[:]
    wq = []  # 이번에 물로 변한곳을 집어넣어줌
    while w:
        x,y = w.pop() # 지점값이 0이 아니면 돌이거나 방문한점이니 바꺼줄 필요없음
        if x-1 >=0 and v[x-1][y] == 0 and (x-1,y) != end:
            v[x-1][y] = -1
            wq.append((x-1,y))
        if x+1 < n and v[x+1][y] == 0 and (x+1,y) != end:
            v[x+1][y] = -1
            wq.append((x+1,y))
        if y - 1 >= 0 and v[x][y-1] == 0 and (x,y-1) != end:
            v[x][y-1] = -1
            wq.append((x,y-1))
        if y+1 < m and v[x][y+1] == 0 and (x,y+1) != end:
            v[x][y+1] = -1
            wq.append((x,y+1))


wq = []
q = []
n,m = map(int,input().split())
name = sys.stdin.read().splitlines()
L = [list(name[idx]) for idx in range(n)]
v = [[0]*m for _ in range(n)]
for i in range(n):  # v 초기화
    for j in range(m):
        if L[i][j] == "S":
            start = (i,j)
        if L[i][j] == "D":
            end = (i,j)
        if L[i][j] == ".": # 지나갈수 있는 통로는 0
            v[i][j] = 0
        elif L[i][j] == "*": # 물이 있는곳은 -1
            v[i][j] = -1
            wq.append((i,j))
        else:  # 돌이 있는곳은 -2
            v[i][j] = -2
v[start[0]][start[1]] = 1
v[end[0]][end[1]] = 0
q.append(start)
depth = 0
while q:
    x,y = q.pop(0)
    if (x,y) == end:
        print(v[x][y]-1)
        exit()
    if v[x][y] != depth:
        make_water()
        depth += 1
    if x - 1 >= 0 and v[x - 1][y] == 0: # 0이 아니면 방문했거나 물 or 돌이므로
        v[x - 1][y] = v[x][y] + 1
        q.append((x - 1, y))
    if x + 1 < n and v[x + 1][y] == 0:
        v[x + 1][y] = v[x][y] + 1
        q.append((x + 1, y))
    if y - 1 >= 0 and v[x][y - 1] == 0:
        v[x][y - 1] = v[x][y] + 1
        q.append((x, y - 1))
    if y + 1 < m and v[x][y + 1] == 0:
        v[x][y + 1] = v[x][y] + 1
        q.append((x, y + 1))
print("KAKTUS")
