# https://programmers.co.kr/learn/courses/30/lessons/17679

def solution(n, m, board):
    board = [list(x) for x in board]
    matched = True
    while matched:
        matched = []
        for i in range(n-1):
            for j in range(m-1):
                if board[i][j] == board[i+1][j]\
                == board[i][j+1] == board[i+1][j+1] != "#":
                    matched.append([i,j])
        for i, j in matched:
            board[i][j] = board[i+1][j]= board[i][j+1]\
                = board[i+1][j+1] = "#"
        for i in range(n-1,-1,-1):
            for j in range(m):
                if board[i][j] == "#":
                    temp = i
                    while temp >= 0 and board[temp][j] == "#":
                        temp -= 1
                    if temp != -1:
                        board[i][j], board[temp][j] = board[temp][j], board[i][j]
    return sum([x.count("#") for x in board])


#  L = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
L = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(4, 5, L))











