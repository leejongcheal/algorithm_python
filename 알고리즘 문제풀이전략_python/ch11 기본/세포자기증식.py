# 문제를 이해해야 하는문제
# 하나의 확정된 값을 가지고 c = a + b -> b = c - a 로 치환해서 푸는 문제
def solve(L, n):
    split = 0
    flag = 0
    L.append([0] * n)
    while True:
        L[1 - flag][n - 2] = L[flag][n - 1]
        for i in range(n - 4, -1, -2):
            L[1 - flag][i] = L[flag][i + 1] - L[1 - flag][i + 2]
        if n % 2 == 0:
            j = 1
            L[1 - flag][1] = L[flag][0] - L[1 - flag][0]
        else:
            j = 0
            L[1 - flag][0] = L[flag][0] - L[1 - flag][1]
        for i in range(j + 2, n, 2):
            L[1 - flag][i] = L[flag][i - 1] - L[1 - flag][i - 2]
        print(L[1 - flag])
        for i in range(n):
            if L[1 - flag][i] < 0:
                flag = -1
                break
        if flag == -1:
            break
        split += 1
        #print(L[1 - flag])
        flag = 1 - flag
    print("++++++++++++++++++++++++++++")
    if split == 0:
        print("-1회 분할")
    else:
        print("%d회 분할" % split)


T = int(input())
for _ in range(T):
    n = int(input())
    L = [list(map(int, input().split()))]
    solve(L, n)
