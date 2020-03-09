import sys


def solve(x, y):
    global L, n
    if x >= n or y >= n:
        return 0
    if x == n - 1 and y == n - 1:
        return 1
    jump = L[x][y]
    return solve(x + jump, y) or solve(x, y + jump)


read = sys.stdin.readline
T = int(read())
for _ in range(T):
    n = int(read())
    L = []
    for _ in range(n):
        L.append(list(map(int, read().split())))
    if solve(0, 0) == 0:
        print("NO")
    else:
        print("YES")
