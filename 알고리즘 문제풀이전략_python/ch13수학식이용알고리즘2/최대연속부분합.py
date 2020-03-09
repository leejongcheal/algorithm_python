def solve(L):
    Max = L[0]
    n = len(L)
    R = [0]*n
    R[0] = L[0]
    print("Max 값이 %d 로 변경됨"%Max)
    for i in range(1,n):
        if R[i-1] + L[i] > L[i]:
            R[i] = R[i-1] + L[i]
        else:
            R[i] = L[i]
        if Max < R[i]:
            Max = R[i]
            print("Max 값이 %d 로 변경됨"%Max)
        #Max = max(Max, R[i])
    print(Max)


T = int(input())
for _ in range(T):
    n = int(input())
    L = list(map(int,input().split()))
    solve(L)
