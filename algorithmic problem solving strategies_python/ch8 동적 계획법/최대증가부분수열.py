# C 50 N 500 2초 -> N^2 일단 4만개를 넘어가니 힘들꺼 같음 nlogn이하로 풀어야함
# LIS 일단 DP인것은 알겠음!
# 초기꺼는 N!의 시간복잡도를 가지는거 같음 따라서 다른 방법 생각, 두번쨰꺼는 n^2의 시간복잡도(이게 바로 DP!)
# 근데 n^2로 충분히 풀림 ㅋㅋㅋ에라이


import sys


def solve(start):
    global L, S, n
    if S[start] != 0:
        return S[start]
    res = 1
    for next in range(start + 1, n):
        if L[start] < L[next]:
            res = max(res, 1 + solve(next))
    S[start] = res
    return res


read = sys.stdin.readline
T = int(read())
for _ in range(T):
    n = int(read())
    L = list(map(int, read().split()))
    S = [0] * n
    maxlen = 1
    for i in range(n):
        maxlen = max(solve(i), maxlen)
    print(maxlen)
