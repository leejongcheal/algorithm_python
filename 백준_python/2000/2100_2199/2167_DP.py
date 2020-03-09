import sys
read = sys.stdin.readline
N, M = map(int, read().split())
dp = []
for i in range(N + 1):
    dp.append([0] * (M + 1))
idx = 0
for i in range(1, N+1):
    L = (list(map(int, read().split())))
    idx += 1
    for j in range(1, M+1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + L[j - 1]
k = int(read())
idx += 1
for _ in range(idx, idx + k):
    x1, y1, x2, y2 = map(int, read().split())
    a = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
    print(a)
