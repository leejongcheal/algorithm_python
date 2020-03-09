N, K = map(int, input().split())
L = list(map(int, input().split()))
for i in range(0,N-K+1):
    a = L[i]
    for j in range(1,K):
        a += L[i+j]
    if i == 0:
        max = a
    if max < a:
        max = a
print(max)
