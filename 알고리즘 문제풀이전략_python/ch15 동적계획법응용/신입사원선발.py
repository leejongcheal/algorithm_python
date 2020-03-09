T = int(input())
for _ in range(T):
    n = int(input())
    L = list(map(int, input().split()))
    S = sorted(L, reverse=True)
    for i in L:
        print(S.index(i) + 1, end=" ")
    print()
