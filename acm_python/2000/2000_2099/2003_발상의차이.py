N, M = map(int, input().split())
n = list(map(int, input().split()))
result = 0
i = 0
sum = 0
for j in range(N):
    sum += n[j]
    if sum >= M:
        while sum >= M:
            if sum == M:
                result += 1
            sum -= n[i]
            i += 1
print(result)
