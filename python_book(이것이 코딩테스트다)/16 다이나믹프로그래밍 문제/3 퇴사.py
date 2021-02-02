N = int(input())
L = []
for _ in range(N):
    t, p = map(int ,input().split())
    L.append((t,p))
dp = [0]*(N+5)
max_value = 0
for i in range(N):
    t, p = L[i]
    dp[i] = max(dp[i], max_value)
    if i + t < N+1:
        dp[i+t] = max(dp[i] + p, dp[i+t])
    if dp[i] > max_value:
        max_value = dp[i]
print(max(dp))
