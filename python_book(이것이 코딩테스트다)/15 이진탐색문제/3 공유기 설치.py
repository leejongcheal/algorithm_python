N, C = map(int, input().split())
L = []
for _ in range(N):
    L.append(int(input()))
L.sort()
start = 0
end = L[-1] - L[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    now_index = 0
    c_cnt = 1
    for i in range(1,N):
        if L[i] - L[now_index] >= mid:
            c_cnt += 1
            now_index = i
    # c가 딱떨어지지않는경우도 생각
    if c_cnt <= C:
        if mid > result:
            result = mid
        start = mid + 1
    elif c_cnt < C:
        end = mid - 1
print(result)


