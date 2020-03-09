# 와 +3에서 결국에 4번 누르면 똑같은걸 가지고 무한조합이 아닌 유한조합으로
# 이힌트를 가지고 브루트 포스 풀이하는데 또 훌룡한게
# swhith10이면 안되니깐 확인해서 ok 0반환 아니면 큰값 반환(불가능)
# 그냥 완벽히 이해 필요
import sys


def areAligned(L):
    for i in range(16):
        if L[i] % 12 != 0:
            return 0
    return 1


def push(L, swith):
    global link
    for i in range(16):
        if link[swith][i] == 'x':
            L[i] += 3


def solve(L, swith):
    global INF
    if swith == 10:
        if areAligned(L) == 1:
            return 0
        else:
            return INF
    ret = INF
    for cnt in range(4):
        ret = min(ret, cnt + solve(L, swith + 1))
        push(L, swith)
    return ret


link = ["xxx.............",
        "...x...x.x.x....",
        "....x.....x...xx",
        "x...xxxx........",
        "......xxx.x.x...",
        "x.x...........xx",
        "...x..........xx",
        "....xx.x......xx",
        ".xxxxx..........",
        "...xxx...x...x.."]
INF = 100000
T = int(input())
read = sys.stdin.readline
for _ in range(T):
    L = list(map(int, read().split()))
    res = solve(L, 0)
    if res >= INF:
        print(-1)
    else:
        print(res)
