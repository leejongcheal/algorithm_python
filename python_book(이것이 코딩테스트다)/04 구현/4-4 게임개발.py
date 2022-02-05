"""
구현중에 쉬운편인데 확실히 구현은 문제이해랑 예외체크에 신경을 많이 써야하는거 같다. 몇번을 틀렸는지
4방향 다확인후에 뒤로가는것도 3방향만 보고 뒤로가는걸로 그냥 넘겨버리고 1,1시작이 -> 0,0 시작을 다르게 말하는줄로 알아먹고
nd 와 d를 써야하는 경우가 있는데 흐름이 아닌 습관적으로 nd만 계속쓰는등 확실히 피지컬이 많이 딸리는것을 많이 느낌
개같다 진짜로..
++ 방향도 시계로 풀었네 아 ㅋㅋ
마지막 배울점 visit 배열을 써도 되는데 L에 방문점을 2로 주어서 풀어도됨
while 1대신 while flag 사용도 배우고
"""
steps = [(-1, 0),(0 , 1),(1, 0),(0, -1)]
N, M = map(int, input().split())
x, y, d = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
count = 1
L[x][y] = 2
flag = 1 # 회전후 이동 or 뒤로 간경우 1로 둘것
while flag:
    flag = 0
    # 회전후 이동하는지 확인
    for i in range(1, 5): # 1  2 3 만 확인 -> 4도 확인해야 ..
        nd = ( d - i) % 4
        nx, ny = x + steps[nd][0], y + steps[nd][1]
        if 0 <= nx < N and 0 <= ny < M and L[nx][ny] == 0:
            flag = 1
            count += 1
            L[nx][ny] = 2
            print(x, y, d, nx, ny, nd, "회전후 이동")
            x, y, d = nx, ny, nd
            break
    # 다 회전후에 뒤로 갈수 있는지 확인
    if flag == 0: # 회전후 이동 안한 경우
        nx, ny = x - steps[d][0], y - steps[d][1]
        if 0 <= nx < N and 0 <= ny < M and L[nx][ny] != 1:
            flag = 1
            print(x,y,nx, ny,"뒤이동")
            x, y = nx, ny
print(count)


