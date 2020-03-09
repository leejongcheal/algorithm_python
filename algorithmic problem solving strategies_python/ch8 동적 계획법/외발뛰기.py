# 메모리 제이션 사용
# 그냥 재귀호출하는데 재사용되는경우가 있을때 메모리제이션 발상해야함
import sys


def solve(x, y):
    global L, n, dic
    if x >= n or y >= n:
        return 0
    if x == n - 1 and y == n - 1:
        return 1
    if dic.get((x, y), -1) != -1:
        return dic[(x, y)]
    else:
        jump = L[x][y]
        dic[(x, y)] = (solve(x + jump, y) or solve(x, y + jump))
        return dic[(x, y)]


read = sys.stdin.readline
T = int(read())
for _ in range(T):
    n = int(read())
    L = []
    dic = dict()
    for _ in range(n):
        L.append(list(map(int, read().split())))
    if solve(0, 0) == 0:
        print("NO")
    else:
        print("YES")
