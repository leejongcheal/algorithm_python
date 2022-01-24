from bisect import bisect_left, bisect_right
N = int(input())
L = list(map(int, input().split()))
L = L[::-1]
result = [L[0]]
for i in range(1,N):
    index = bisect_left(result, L[i])
    if index >= len(result):
        result.append(L[i])
    else:
        result[index] = L[i]
print(N - len(result))

