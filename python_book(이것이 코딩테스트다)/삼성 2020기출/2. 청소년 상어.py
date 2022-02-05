from collections import deque
steps = [(-1, 0),(-1, -1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
def move_fish(L):
    #  물고기 번호순 이동
    for fish_number in range(1, 17):
        flag = 0
        for i in range(4):
            for j in range(4):
                if L[i][j][0] == fish_number:
                    x, y = i, j
                    d = L[i][j][1]
                    flag = 1
        if flag == 0:
            # 물고기번호 없는 경우 무시
            continue
        for plusd in range(8):
            nd = (d + plusd) % 8
            dx, dy = steps[nd]
            nx, ny = x + dx, y+ dy
            if 0 <= nx < 4 and 0 <= ny < 4 and L[nx][ny][0] != -1:
                L[x][y] = (fish_number, nd)
                L[x][y], L[nx][ny] = L[nx][ny], L[x][y]
                break





def deep_copy(L):
    temp = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            temp[i][j] = L[i][j]
    return temp

L = [[0]*4 for _ in range(4)]
for i in range(4):
    a1, d1, a2, d2, a3, d3, a4, d4 = map(int, input().split())
    d1, d2, d3, d4 = d1 -1 , d2 -1 ,d3 - 1, d4 - 1
    L[i][0] = (a1, d1)
    L[i][1] = (a2, d2)
    L[i][2] = (a3, d3)
    L[i][3] = (a4, d4)
res = L[0][0][0]
x, y = 0, 0
d = L[0][0][1]
L[0][0] = (-1, d)
q = deque()
q.append((L,x,y,d,res))
while q:
    L, x, y, d, total = q.popleft()
    res = max(res, total)
    move_fish(L)
    # 상어 이동 가능한경우 다 q에 넣기
    for i in range(1, 4):
        dx, dy = steps[d]
        nx, ny = x + dx*i, y + dy*i
        if 0 <= nx < 4 and 0 <= ny < 4 and L[nx][ny][0] > 0:
            temp = deep_copy(L)
            temp[x][y] = (0, d)
            get_fish = temp[nx][ny]
            temp[nx][ny] = (-1, get_fish[1])
            q.append((temp,nx,ny,get_fish[1], total + get_fish[0]))
print(res)