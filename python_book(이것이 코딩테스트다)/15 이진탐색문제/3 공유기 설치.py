def binary_search(L):
    global N, res
    start, end = 0, L[-1] - L[0]
    while start <= end:
        mid = (start + end) // 2
        if check(mid) == 1:
            res = max(res, mid)
            start = mid + 1
        else:
            end = mid - 1

def check(target):
    global L, N, C
    now_c = 0
    cnt_c = 1
    for i in range(1, N):
        if L[i] - L[now_c] >= target:
            now_c = i
            cnt_c += 1
        if cnt_c >= C:
            return 1
    return 0

N, C = map(int, input().split())
L = []
for _ in range(N):
    L.append(int(input()))
L.sort()
res = 0
binary_search(L)
print(res)