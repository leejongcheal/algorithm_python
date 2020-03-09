N = int(input())
L = list(map(int, input().split()))
L.sort()
res = 0
for i in range(1, N):
    res += (N-i)*i*(L[i] - L[i-1])
print(res*2)
