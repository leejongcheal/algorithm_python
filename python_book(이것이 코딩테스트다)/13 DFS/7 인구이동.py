from collections import deque
# 주어진 x,y 에 대해 덩어리를 만들고 숫자기록
# 덩어리 있으면 1 없으면 0 리턴
def BFS(i,j):
    global A, L, R, N, visit
    steps = [(1,0),(-1,0),(0,1),(0,-1)]
    cnt = 1
    set_sum = A[i][j]
    set_List = [(i, j)]
    q = deque()
    visit.append((i, j))
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for step in steps:
            nx, ny = x + step[0], y+ step[1]
            if 0 <= nx < N and 0 <= ny < N:
                if L <= abs(A[x][y] - A[nx][ny]) <= R and (nx,ny) not in visit:
                    q.append((nx, ny))
                    visit.append((nx, ny))
                    cnt += 1
                    set_sum += A[nx][ny]
                    set_List.append((nx, ny))
    if cnt != 1:
        averege = int(set_sum / cnt)
        for set in set_List:
            x, y = set[0], set[1]
            A[x][y] = averege
        return 1
    else:
        return 0



N, L, R = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
result = 0
while 1:
    flag = 0
    visit = []
    for i in range(N):
        for j in range(N):
            if (i,j) not in visit:
                if BFS(i,j) == 1:
                    flag = 1
    if flag == 0:
        break
    else:
        result += 1
print(result)