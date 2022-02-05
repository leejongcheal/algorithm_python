# 주어진 높이의 합값이 target보다 큰지 비교
# 같으면 0 작으면 -1 크면 1
def l_sum(L, mid, target):
    sum = 0
    for i in L[::-1]:
        if i > mid:
            sum += i - mid
        else:
            break
    if sum == target:
        return 0
    elif sum > target:
        return 1
    else:
        return -1


def binary_serach(L, target, start, end):
    global M
    if start > end:
        return M
    mid = (start + end) // 2
    sum = l_sum(L, mid, target)
    if sum == 0:
        M = mid
        return M
    elif sum == 1:
        start = mid + 1
        if mid > M:
            M = mid
    else:
        end = mid - 1
    return binary_serach(L,target, start, end)


n, m = map(int, input().split())
L = list(map(int, input().split()))
L.sort()
start = 0
end = L[-1] #굳이 2억개를 할필요없이 가진겂의 최대값으로 해도됨
M = 0
binary_serach(L, m, start, end)
print(M)