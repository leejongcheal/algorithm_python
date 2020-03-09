# 전꺼는 시간초과 온라인 알고리즘으로 한번 짜보자
# 체감적으로 조금더 빨라진거같음
# 그래도 안됨
from collections import deque
import sys


def rng():
    global seed, mod
    ret = seed
    seed = (seed * 214013 + 2531011) % mod
    return ret % 10000 + 1


read = sys.stdin.readline
T = int(read())
mod = 2 ** 32
maxn = 0  # 5000000
L = [1983]
A = []
ans = []
for _ in range(T):
    k, n = map(int, read().split())
    sum = 0
    res = 0
    seed = 1983
    q = deque()
    for i in range(n):
        newSignal = rng()
        q.append(newSignal)
        sum += newSignal
        if sum > k:
            while sum > k:
                sum -= q.popleft()
        if sum == k:
            res += 1
    print(res)
#     ans.append(res)
# for a in ans:
#     sys.stdout.write("{}\n".format(a))
