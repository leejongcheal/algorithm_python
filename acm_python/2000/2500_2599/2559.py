import sys
input = sys.stdin.readline
N, K = map(int,input().split())
L = list(map(int,input().split()))
sum = sum(L[:K])
res = sum
for i in range(K,N):
    sum -= L[i - K]
    sum += L[i]
    res = max(sum, res)
print(res)
