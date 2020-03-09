T = int(input())
for _ in range(T):
    n = int(input())
    L= []
    for i in range(n):
        L.append(int(input()))
    sum = 0
    for i in range(1,n):
        for j in range(0,i):
            sum += 2*(abs(L[i] - L[j]))
    print(sum)

