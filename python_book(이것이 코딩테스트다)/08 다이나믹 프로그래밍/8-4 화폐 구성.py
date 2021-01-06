n, m = map(int, input().split())
L = []
for i in range(n):
    L.append(int(input()))
result = [1e9]*(m+1)
for x in L:# 이거 자체가 m의 크기를 넘어가는 경우의수를 생각못함
    if x < m+1:
        result[x] = 1
for i in range(m+1):
    for x in L:
        if i - x > 0 and result[i-x] != 1e9:
            result[i] = min(result[i-x]+1, result[i])
if result[m] != 1e9:
    print(result[m])
else:
    print(-1)
# print(result)