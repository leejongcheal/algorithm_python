T = int(input())
for _ in range(T):
    n = int(input())
    L = []
    for i in range(n):
        L.append(list(map(float, input().split())))
    i = 0
    print(i+1, end=" ")
    while True:
        max = -100000
        for j in range(i + 1, n):
            ratio = (L[j][1] - L[i][1]) / (L[j][0] - L[i][0])
            if ratio > max:
                max = ratio
                sol = j
        print(sol+1, end=" ")
        i = sol
        if i == n-1:
            break
    print()
