T = int(input())
for _ in range(T):
    N, Q = map(int,input().split())
    L = []
    for i in range(N):
        L.append(int(input()))
    for i in range(Q):
        x, y = map(int, input().split())
        print(min(L[x-1:y]))
