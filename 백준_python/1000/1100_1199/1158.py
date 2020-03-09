N,M = map(int,input().split())
L = []
R = []
for i in range(1,N+1):
    L.append(i)
i = 0
while L:
    if i == len(L):
        i = 0
    for c in range(M-1):
        i += 1
        if i == len(L):
            i = 0
    R.append(L[i])
    del L[i]
if N > 1:
    print("<",end="")
    for i in range(N - 1):
        print(R[i],end=", ")
    print(str(R[i+1])+">")
else:
    print("<{}>".format(R[0]))
