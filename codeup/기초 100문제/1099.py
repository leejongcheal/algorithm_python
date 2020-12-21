import sys


def BFS(x,y):
    global L, flag
    if L[x][y] == 2:
        L[x][y] = 9
        flag = 1
        return
    if y+1 < 10 and flag == 0 and L[x][y+1] != 1:
        BFS(x,y+1)
    elif x+1 < 10 and flag == 0 and L[x+1][y] != 1:
        BFS(x+1,y)
    L[x][y] = 9
    return

L = []
flag = 0
for _ in range(10):
    L.append(list(map(int, sys.stdin.readline().rstrip().split())))
BFS(1, 1)
for i in range(10):
    print(" ".join((map(str,L[i]))))

