# https://programmers.co.kr/learn/courses/30/lessons/17679

def solution(n, m, board):
    for i in range(n):
        board[i] = list(board[i])
    answer = 0
    while 1:
        X_set = set()
        for i in range(n-1):
            for j in range(m-1):
                if board[i][j] != "X":
                    if board[i][j] == board[i+1][j]\
                    == board[i][j+1] == board[i+1][j+1]:
                        X_set.add((i,j))
                        X_set.add((i+1,j))
                        X_set.add((i,j+1))
                        X_set.add((i+1,j+1))
        if not X_set:
            break
        else:
            answer += len(X_set)
        for i, j in X_set:
            board[i][j] = "X"
        for i in range(n-1,-1,-1):
            for j in range(m):
                if board[i][j] == "X":
                    temp = i
                    while temp >= 0 and board[temp][j] == "X":
                        temp -= 1
                    if temp != -1:
                        board[i][j], board[temp][j] = board[temp][j], board[i][j]
    return answer