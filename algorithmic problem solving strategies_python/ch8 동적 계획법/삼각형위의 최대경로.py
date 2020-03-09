# 합을 구하는게 아닌 경로를 구하는 문제도 있음 ㅋㅋㅋ
# 이번엔 합을 구하는걸로 메모리제이션 사용을 할수있다는것을 숙지해야함!
import sys


def solve(x, y):
    global n, L
    if x + 1 == n:
        return L[x][y]
    if dic.get((x, y), -1) != -1:
        return dic[(x, y)]
    dic[(x, y)] = max(solve(x + 1, y), solve(x + 1, y + 1)) + L[x][y]
    return dic[(x, y)]


read = sys.stdin.readline
T = int(read())
for _ in range(T):
    n = int(read())
    L = []
    dic = dict()
    for _ in range(n):
        L.append(list(map(int, read().split())))
    print(solve(0, 0))
