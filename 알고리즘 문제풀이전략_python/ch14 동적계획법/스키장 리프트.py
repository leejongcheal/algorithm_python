def solve(n, L):
    R = [0] * (n + 1)
    for i in range(1,n+1):
        R[i] = L[0]*i
    #print(R)
    for i in range(0, n+1):
        for j in range(10):
            if i + j + 1 > n:
                break
            if R[i + j + 1] > R[i] + L[j]:
                R[i + j + 1] = R[i] + L[j]
    print(R[n])


T = int(input())
for _ in range(T):
    L = list(map(int, input().split()))
    solve(int(input()), L)
