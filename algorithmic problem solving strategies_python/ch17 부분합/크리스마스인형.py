def solve_max(x):
    global Psum, maxBuy, n, k
    max_temp = -1
    for i in range(0, x):
        if Psum[x] % k == Psum[i] % k:
            max_temp = i
    if max_temp >= 0:
        maxBuy[x] = max(maxBuy[x - 1], maxBuy[max_temp] + 1)
    else:
        maxBuy[x] = maxBuy[x - 1]


T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    L = list(map(int, input().split()))
    Psum = [0]
    sum = 0
    buy = 0
    maxBuy = [0] * (n + 1)
    for i in range(n):
        sum += L[i]
        Psum.append(sum)
    for i in range(1, n + 1):
        for j in range(i):
            if Psum[i] % k == Psum[j] % k:
                buy += 1
    for i in range(1, n + 1):
        solve_max(i)
    print(buy, maxBuy[n])

