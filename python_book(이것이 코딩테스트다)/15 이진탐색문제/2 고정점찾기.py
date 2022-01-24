N = int(input())
L = list(map(int,input().split()))

# 이진탐색 시작
start = 0
end = N - 1
res = -1
while 1:
    if start > end:
        break
    mid = (start + end) // 2
    if L[mid] == mid:
        res = mid
        break
    elif L[mid] > mid:
        end = mid-1
    else:
        start = mid + 1
print(res)
