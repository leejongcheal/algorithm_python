# 거꾸로 가는거랑 별 차이 없을줄 알았는데
# 코드에서 간편하고 메모리 관련해서 훨씬 좋음 in-place 메모리
def solve(L, n):
    R = []
    for i in range(n):
        R.append([0] * (i + 1))
    R[0][0] = L[0][0]
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                R[i][j] = R[i - 1][j] + L[i][j]
            elif j == i:
                R[i][j] = R[i - 1][j - 1] + L[i][j]
            else:  # j-1 >= 0 and j <= i
                R[i][j] = max(R[i - 1][j], R[i - 1][j - 1]) + L[i][j]
    print(max(R[n-1]))


T = int(input())
for _ in range(T):
    n = int(input())
    L = []
    for i in range(n):
        L.append(list(map(int, input().split())))
    solve(L, n)
