n = int(input())
x, y = 1, 1
plans = input().split()

# L R U D 에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나지 않는경우에 이동
    if 0 < nx <= n and 0 < ny <= n:
        x, y = nx, ny
print(x, y)