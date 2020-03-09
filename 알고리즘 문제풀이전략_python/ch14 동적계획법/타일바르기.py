# DP문제입니다
# f(n-1) + ? 식의 점화식의 경우 f(n-1)을 한쪽에 치우치고 생각하세요
# 위의 예는 1+f f+1이런식으로 계산 하지말고 f+1의 경우만 생각하라 이것입니다.
T = int(input())
for _ in range(T):
    n = int(input())
    m = int(input())
    L = [0]*(n+3)
    L[0] = 1
    L[1] = 3
    if n > 2:
        for i in range(2,n):
            L[i] = 2*L[i-2] + L[i-1]
    print(L[n-1] % m)
