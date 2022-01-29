N , M = map(int, input().split())
L = list(map(int, input().split()))
data = [0]*(M+1)
res = 0
for i in range(1, M + 1):
    data[i] = L.count(i)
for i in range(1, M):
    res += data[i] * sum(data[i+1:M+1])
print(res)
