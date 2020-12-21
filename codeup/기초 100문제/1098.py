import sys
h, w = map(int, sys.stdin.readline().rstrip().split())
L = [[0]*w for _ in range(h)]
a = int(sys.stdin.readline().rstrip())
for _ in range(a):
    l, d, x, y = map(int, sys.stdin.readline().rstrip().split())
    for i in range(l):
        if d == 0: # 가로
            L[x-1][y-1+i] = 1
        else: # 세로
            L[x-1+i][y-1] = 1
for i in range(h):
    print(" ".join(list(map(str, L[i]))))
