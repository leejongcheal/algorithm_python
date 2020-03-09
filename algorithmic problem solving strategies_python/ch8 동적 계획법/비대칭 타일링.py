# 동적 계획법중 점화식 세우기 문제 같아보임
# 전에 전부세는건 있으니 이를 이용해서 푸는것 까지 이해함
# 그래서 전부세는것을 이용해 비대칭을 셀려고함 (짝홀 a*(a'-1)+ 2*b(b-1))
# 근데 전부에서 대칭인 경우만 뺴는 판단을 못함 와우
import sys


def tiling():
    global tile, maxn, n
    if maxn == 0:
        tile[0] = 0
        tile[1] = 1
        tile[2] = 2
    if maxn < 3:
        maxn = 3
    for i in range(maxn, n+1):
        tile[i] = (tile[i-2] + tile[i-1]) % 1000000007


def solve(n):
    global tile
    if n <= 2:
        return 0
    if n % 2 == 1:
        return (tile[n] - tile[(n-1)//2]) % 1000000007
    else:
        return (tile[n] - (tile[(n-2)//2] + tile[n//2])) % 1000000007


read = sys.stdin.readline
maxn = 0
ans = []
tile = [0]*101
for _ in range(int(read())):
    n = int(read())
    if n > maxn:
        tiling()
        maxn = n
    ans.append(solve(n))
for a in ans:
    sys.stdout.write("{}\n".format(a))
