def distance(x, y):
    if (x[0] - y[0])**2 + (x[1] - y[1])**2 > y[2]**2:
        return 0
    else:
        return 1


t = int(input())
for i in range(t):
    L = []
    L = list(map(int,input().split()))
    # print(L)
    a = [L[0],L[1]]
    b = [L[2],L[3]]
    # print(a,b)
    k = int(input())
    L = []
    for j in range(k):
        L.append(list(map(int,input().split())))
    R1 = []
    R2 = []
    for c in L:
        if distance(a,c) == 1:
            R1.append(c)
        if distance(b,c) == 1:
            R2.append(c)
    r = len(R1)+len(R2)
    for c in R1:
        if c in R2:
            r -= 2
    print(r)
