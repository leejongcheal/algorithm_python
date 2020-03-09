# 와 진짜 멋지다! 와 진짜루 미쳤다 어떻게 발상하냐 아니 진짜 너무하네 이건 ㅋㅋ
# 1ㅁㅁ1 / =ㅁ= / 1ㅁ= / =ㅁ1 의 경우로 a,b는 대칭하니 ㅁ에 대해서 [비대칭으로] 채울수 있는 방법 찾으러
# c,d는 ㅁ을 [그냥] 채울수 있는경우의 수 구하기
import sys


def tiling():
    global tile, maxn, n
    if maxn == 0:
        tile[0] = 1
        tile[1] = 1
        tile[2] = 2
    if maxn < 3:
        maxn = 3
    for i in range(maxn, n+1):
        tile[i] = (tile[i-2] + tile[i-1]) % 1000000007


def solve(n):
    global tile, asy, tile
    if n <= 2:
        return 0
    if asy.get(n,-1) != -1:
        return asy[n]
    # a
    ret = 0
    ret += solve(n-2)
    ret += solve(n-4)
    ret += 2*tile[n-3]
    asy[n] = ret% 1000000007
    return asy[n]


read = sys.stdin.readline
maxn = 0
ans = []
tile = [0]*101
asy = dict()
asy[3] = 3
for _ in range(int(read())):
    n = int(read())
    if n > maxn:
        tiling()
        maxn = n
    ans.append(solve(n))
for a in ans:
    sys.stdout.write("{}\n".format(a))
