def f(N):
    for i in range(1, N//2+1):
        if N % i == 0:
            yield i
    yield N


N, K = map(int, input().split())
L = list(f(N))
try:
    print(L[K - 1])
except:
    print(0)
