n = int(input())
L = list(map(int, input().split()))
result = []
result.append(L[0])
result.append(L[1])
for i in range(2,n):
    result.append(max(result[i-1], result[i-2] + L[i]))
print(result[-1])