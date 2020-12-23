n, m = map(int, input().split())
A, B, d = map(int, input().split())
# 0  1  2  3
# 북 동 남 서 -> 왼족 서 북 동 남 // 반시계라 거꾸로 가면된다. -1 씩 해주면됨
steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
result = 1
L = []
for _ in range(n):
    L.append(list(map(int, input().split())))
# 0 육지 1 바다
visit = [[0] * m for _ in range(n)]
visit[A][B] = 1
while 1:
    move = 0
    # 각 방향 왼쪽 조사
    for i in range(4):
        nd = (d - (i+1))%4
        na = A + steps[nd][0]
        nb = B + steps[nd][1]
        # 이동조건  1) 칸안 2) 방문한적 없는 3) 육지 해당 방향으로 이동
        if 0 <= na < n and 0 <= nb < m and L[na][nb] == 0 and visit[na][nb] == 0:
            A, B, d = na, nb, nd
            # print(A,B,d,"쪽 이동")
            visit[A][B] = 1
            move = 1
            result += 1
            break
    # 이동이 안되서 뒤로 가는 경우
    if move == 0:
        na = A - steps[d][0]
        nb = B - steps[d][1]
        # 뒤로가는 조건 1) 칸안 2) 육지
        if 0 <= na < n and 0 <= nb < m and L[na][nb] == 0:
            A, B = na, nb
            # print(A,B,d,"뒤로이동후 좌표")
        # 멈추는 조건 1) 바다 2) 칸밖
        else:
            # print(A,B,d,"멈춤 좌표")
            break
# for i in visit:
#     print(i)
print(result)
