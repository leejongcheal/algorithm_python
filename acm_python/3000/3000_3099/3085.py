import sys


def check():
    global m,n
    global L
    for x in range(n):
        cnt = 1
        for y in range(n-1):
            if L[x][y] == L[x][y + 1]:
                cnt += 1
            else:
                m = max(cnt, m)
                cnt = 1
        m = max(cnt, m)
        cnt = 1
        for y in range(n-1):
            if L[y][x] == L[y + 1][x]:
                cnt += 1
            else:
                m = max(cnt, m)
                cnt = 1
        m = max(cnt, m)


n = int(input())
input = sys.stdin.readline
L = [list(input().strip()) for _ in range(n)]
# 행검사
m = 0
check()
# 바꾸고 검사 바꾸고 검사하는 식으로 무식하게 ㅅㅂ
for i in range(n):
    for j in range(n):
        if i != j:
            if j+1 < n :
                L[i][j], L[i][j + 1] = L[i][j + 1], L[i][j]
                check()
                L[i][j], L[i][j + 1] = L[i][j + 1], L[i][j]
            if i+1 < n :
                L[i + 1][j], L[i][j] = L[i][j], L[i + 1][j]
                check()
                L[i + 1][j], L[i][j] = L[i][j], L[i + 1][j]
print(m)
