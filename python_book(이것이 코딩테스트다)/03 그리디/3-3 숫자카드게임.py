n, m = map(int, input().split())
result = (-1e9)
for _ in range(n):
    L = list(map(int, input().split()))
    if result < min(L):
        result = min(L)
print(result)