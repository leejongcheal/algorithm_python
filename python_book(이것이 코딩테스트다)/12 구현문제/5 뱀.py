from collections import deque

N = int(input())
L = [[0] * N for _ in range(N)]
# 방향모음
# L -1 D +1
steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
now_d = 0
D = deque()
q = deque()
K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    L[a - 1][b - 1] = 2
d = int(input())
for _ in range(d):
    a, b = input().split()
    D.append((int(a), b))
# 초기화 완료
time = 0
x, y, d = 0, 0, 0
nd = D.popleft()
# 벽 or 몸 만나야 종료
q.append((0,0))
while 1:
    if time == nd[0]:
        if nd[1] == "L":
            d = (d - 1) % 4
        elif nd[1] == "D":
            d = (d + 1) % 4
        if len(D) != 0:
            nd = D.popleft()
    nx = x + steps[d][0]
    ny = y + steps[d][1]
    # 종료 조건인 경우
    if not (0 <= nx < N and 0 <= ny < N) or L[nx][ny] == 1:
        time += 1
        break
    # 사과인 경우
    elif L[nx][ny] == 2:
        L[nx][ny] = 1
    # 단순한 이동
    else:
        last_x, last_y = q.popleft()
        L[last_x][last_y] = 0
        L[nx][ny] = 1
    # 이동한 경우 공통점
    time += 1
    x, y = nx, ny
    q.append((x, y))
print(time)
