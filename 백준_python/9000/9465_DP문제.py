import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    L = []
    DP = [[0]*n for _ in range(2)]
    L.append(list(map(int,input().split())))
    L.append(list(map(int, input().split())))
    DP[0][0] = L[0][0]
    DP[0][1] = L[0][1] + L[1][0]
    DP[1][1] = L[1][1] + L[0][0]
    DP[1][0] = L[1][0]
    for i in range(2,n):
        DP[0][i] = max(DP[1][i-1],DP[1][i-2]) + L[0][i]
        DP[1][i] = max(DP[0][i - 1], DP[0][i - 2]) + L[1][i]
    print(max(DP[0][n-1],DP[1][n-1]))

