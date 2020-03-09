def sum_L(upper_bound):
    global L
    s = 0
    for i in L:
        if i > upper_bound:
            s += upper_bound
        else:
            s += i
    return s


n = int(input())
L = sorted(list(map(int, input().split())))
m = int(input())
if sum(L) <= m:
    print(L[-1])
    exit()
high = m
low = 0
res = []
while low <= high:
    mid = (high + low)//2
    s = sum_L(mid)
    if s > m:
        high = mid - 1
    elif s < m:
        low = mid + 1
        res.append(mid)
    else:
        print(mid)
        exit()
print(max(res))
