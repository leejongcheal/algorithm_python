from bisect import bisect_left, bisect_right
N, X = map(int, input().split())
L = list(map(int, input().split()))
result = bisect_right(L,X) - bisect_left(L, X)
print(result)