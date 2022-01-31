from collections import deque


def solution(board):
    # pass
    N = len(board)
    start = (0, 0, 0, 1)
    q = deque()
    q.append((0, 0, 0, 1, 0))
    steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visit = set()
    visit.add(start)
    dic = dict()
    dic[(1, 0)] = [[(0, -1), (1, 0)], [(0, 1), (1, 0)]]
    dic[(0, -1)] = [[(-1, 0), (0, -1)], [(1, 0), (0, -1)]]
    dic[(-1, 0)] = [[(0, -1), (-1, 0)], [(0, 1), (-1, 0)]]
    dic[(0, 1)] = [[(-1, 0), (0, 1)], [(1, 0), (0, 1)]]
    while q:
        x1,y1, x2,y2, dist = q.popleft()
        if (x1 == N - 1 and y1 == N - 1) or (x2 == N - 1 and y2 == N - 1):
            return dist
        #stpes에 대해서
        for dx,dy in steps:
            nx1, ny1, nx2, ny2 = x1 +dx, y1 +dy, x2 + dx, y2 + dy
            next = (nx1, ny1, nx2, ny2, dist + 1)
            if 0 <= nx1 < N and 0 <= ny1 < N and 0 <= nx2 < N and 0 <= ny2 < N and (nx1, ny1, nx2, ny2) not in visit:
                if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
                    visit.add((nx1, ny1, nx2, ny2))
                    q.append(next)
        # a - b에 대해서
        d1 = (x1 - x2, y1 - y2)
        for d_list in dic[d1]:
            flag = 0
            nx2, ny2 = x2, y2
            for i in range(2):
                dx, dy = d_list[i]
                nx2, ny2 = nx2 + dx, ny2 + dy
                if i == 0:
                    if 0 <= nx2 < N and 0 <= ny2 < N:
                        if board[x1][y1] == 0 and board[nx2][ny2] == 0:
                            continue
                        else:
                            flag = 1
                    else:
                        flag = 1
                elif i == 1:
                    if 0 <= nx2 < N and 0 <= ny2 < N and (x1, y1, nx2, ny2) not in visit and flag == 0:
                        if board[x1][y1] == 0 and board[nx2][ny2] == 0:
                            visit.add((x1, y1, nx2, ny2))
                            q.append((x1, y1, nx2, ny2, dist + 1))
        # b - a에 대해서
        d2 = (x2 - x1, y2 - y1)
        for d_list in dic[d2]:
            flag = 0
            nx1, ny1 = x1, y1
            for i in range(2):
                dx, dy = d_list[i]
                nx1, ny1 = nx1 + dx, ny1 + dy
                if i == 0:
                    if 0 <= nx1 < N and 0 <= ny1 < N:
                        if board[nx1][ny1] == 0 and board[x2][y2] == 0:
                            continue
                        else:
                            flag = 1
                    else:
                        flag = 1
                elif i == 1:
                    if 0 <= nx1 < N and 0 <= ny1 < N and (nx1, ny1, x2, y2) not in visit and flag == 0:
                        if board[nx1][ny1] == 0 and board[x2][y2] == 0:
                            visit.add((nx1, ny1, x2, y2))
                            q.append((nx1, ny1, x2, y2, dist + 1))


# N = int(input())
# board = []
# for _ in range(N):
#     board.append(list(map(int, input().split())))
board = [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0],
         [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]
# board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))
