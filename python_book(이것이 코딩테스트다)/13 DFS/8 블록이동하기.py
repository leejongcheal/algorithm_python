from collections import deque


def solution(board):
    answer = 0
    steps = [(1, 0, 1, 0), (-1, 0, -1, 0), (0, 1, 0, 1), (0, -1, 0, -1)]
    # 이동 좌표 확인 좌표 순
    rotation = [(1, 1, 1, 0), (-1, 1, 0, 1), (-1, -1, -1, 0), (1, -1, 0, -1)]
    re_rotation = [(-1, 1, -1, 0), (-1, -1, 0, -1), (1, -1, 1, 0), (1, 1, 0, 1)]
    # 기준 - 이동 x y 좌표
    direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    N = len(board)
    a = (0, 0)
    b = (0, 1)
    q = deque()
    move = 0
    q.append((a, b, move))
    visit = set()
    visit.add((a, b))
    while q:
        # print(q)
        a, b, move = q.popleft()
        ax, ay = a
        bx, by = b
        if (ax == N - 1 and ay == N - 1) or (bx == N - 1 and by == N - 1):
            return move
        # 상하좌우
        for step in steps:
            nax, nay = ax + step[0], ay + step[1]
            na = (nax, nay)
            nbx, nby = bx + step[2], by + step[3]
            nb = (nbx, nby)
            # print(na,nb)
            if 0 <= nax < N and 0 <= nay < N and 0 <= nbx < N and 0 <= nby < N:
                if board[nax][nay] == 0 and board[nbx][nby] == 0 and (na, nb) not in (visit):
                    q.append((na, nb, move + 1))
                    visit.add((na, nb))
        # a 기준
        pivot = (ax - bx, ay - by)
        for i in range(4):
            if direction[i][0] == pivot[0] and direction[i][1] == pivot[1]:
                d = i
        # 시계 반시계 순서
        mx, my, cx, cy = rotation[d]
        nbx, nby, cbx, cby = bx + mx, by + my, bx + cx, by + cy
        if 0 <= nbx < N and 0 <= nby < N and 0 <= cbx < N and 0 <= cby < N:
            nb = (nbx, nby)
            if board[nbx][nby] == 0 and board[cbx][cby] == 0 and (a, nb) not in (visit):
                q.append((a, nb, move + 1))
                visit.add((a, nb))
        # 반시계
        mx, my, cx, cy = re_rotation[d]
        nbx, nby, cbx, cby = bx + mx, by + my, bx + cx, by + cy
        if 0 <= nbx < N and 0 <= nby < N and 0 <= cbx < N and 0 <= cby < N:
            nb = (nbx, nby)
            if board[nbx][nby] == 0 and board[cbx][cby] == 0 and (a, nb) not in (visit):
                q.append((a, nb, move + 1))
                visit.add((a, nb))
        # b 기준
        pivot = (bx - ax, by - ay)
        for i in range(4):
            if direction[i][0] == pivot[0] and direction[i][1] == pivot[1]:
                d = i
        mx, my, cx, cy = rotation[d]
        nax, nay, cax, cay = ax + mx, ay + my, ax + cx, ay + cy
        if 0 <= nax < N and 0 <= nay < N and 0 <= cax < N and 0 <= cay < N:
            na = (nax, nay)
            if board[nax][nay] == 0 and board[cax][cay] == 0 and (na, b) not in(visit):
                q.append((na, b, move + 1))
                visit.add((na, b))
        mx, my, cx, cy = re_rotation[d]
        nax, nay, cax, cay = ax + mx, ay + my, ax + cx, ay + cy
        if 0 <= nax < N and 0 <= nay < N and 0 <= cax < N and 0 <= cay < N:
            na = (nax, nay)
            if board[nax][nay] == 0 and board[cax][cay] == 0 and (na, b) not in (visit):
                q.append((na, b, move + 1))
                visit.add((na, b))


# N = int(input())
# board = []
# for _ in range(N):
#     board.append(list(map(int, input().split())))
board= [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]
print(solution(board))
